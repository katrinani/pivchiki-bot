import numpy as np
import psycopg2
from ..postgres import config  # Изменен импорт

class CollaborativeFilteringRecommender:
    def __init__(self):
        """Инициализирует класс и устанавливает соединение с базой данных."""
        self.conn = self._connect_to_db()

    def _connect_to_db(self):
        """Устанавливает соединение с базой данных PostgreSQL."""
        conn = None
        try:
            conn = psycopg2.connect(
                host=config.config_db["host"],
                database=config.config_db["dbname"],
                user=config.config_db["user"],
                password=config.config_db["password"]
            )
            print("CollaborativeFilteringRecommender: Успешно подключено к базе данных!")
        except psycopg2.Error as e:
            print(f"CollaborativeFilteringRecommender: Ошибка подключения к базе данных: {e}")
        return conn

    async def get_all_users(self):
        """Получает всех пользователей и их UserId."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT UserId FROM Users;")
            users = [row[0] for row in cursor.fetchall()]
            return users
        except Exception as e:
            print(f"Ошибка при получении пользователей: {e}")
            return []
        finally:
            cursor.close()

    async def get_user_similarity_vector(self, user_id: int):
        """Получает вектор сходства пользователя из базы данных."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT CollaborativeFilteringResults FROM Users WHERE UserId = %s;", (user_id,))
            result = cursor.fetchone()
            if result and result[0]:
                return np.array(result[0])
            else:
                return None
        except Exception as e:
            print(f"Ошибка при получении вектора сходства пользователя {user_id}: {e}")
            return None
        finally:
            cursor.close()

    async def get_user_rated_tracks(self, user_id: int):
        """Получает список TrackId, которые пользователь оценил."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT TrackId FROM UserTrackRatings WHERE UserId = %s AND Rating != 0;", (user_id,)) # Учитываем -1 и 1
            rated_tracks = [row[0] for row in cursor.fetchall()]
            return set(rated_tracks)
        except Exception as e:
            print(f"Ошибка при получении оцененных треков пользователя {user_id}: {e}")
            return set()
        finally:
            cursor.close()

    async def get_top_rated_track_ids_by_similar_users(self, current_user_id: int, similarity_threshold: float = 0.1, top_n: int = 10): # Понижен порог для большего количества соседей
        """Получает top N наиболее высоко оцененных TrackId похожими пользователями."""
        current_user_similarity = await self.get_user_similarity_vector(current_user_id)
        if current_user_similarity is None:
            return []

        all_users = await self.get_all_users()
        similar_users = []
        for user_id in all_users:
            if user_id != current_user_id:
                other_user_similarity = await self.get_user_similarity_vector(user_id)
                if other_user_similarity is not None and current_user_similarity.shape == other_user_similarity.shape:
                    similarity_score = current_user_similarity[all_users.index(user_id)]
                    if similarity_score > similarity_threshold:
                        similar_users.append(user_id)

        if not similar_users:
            return []

        track_ratings_by_similar = {}
        for user_id in similar_users:
            cursor = self.conn.cursor()
            try:
                cursor.execute("""
                    SELECT TrackId, Rating
                    FROM UserTrackRatings
                    WHERE UserId = %s AND Rating != 0;
                """, (user_id,))
                user_ratings = cursor.fetchall()
                for track_id, rating in user_ratings:
                    if track_id not in track_ratings_by_similar:
                        track_ratings_by_similar[track_id] = 0
                    track_ratings_by_similar[track_id] += rating # Суммируем оценки (-1, 1)
            except Exception as e:
                print(f"Ошибка при получении оценок пользователя {user_id}: {e}")
            finally:
                cursor.close()

        sorted_tracks = sorted(track_ratings_by_similar.items(), key=lambda item: item[1], reverse=True)
        current_user_rated = await self.get_user_rated_tracks(current_user_id)
        recommendations_track_ids = [track_id for track_id, _ in sorted_tracks if track_id not in current_user_rated][:top_n]
        return recommendations_track_ids

    async def get_track_paths_by_ids(self, track_ids: list[int]):
        """Получает пути к аудиофайлам треков по их ID."""
        if not track_ids:
            return [], []
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"SELECT Song, Name FROM Tracks WHERE TrackId IN %s;", (tuple(track_ids),))
            tracks_data = cursor.fetchall()
            paths = [row[0] for row in tracks_data]
            names = [row[1] for row in tracks_data]
            return names, paths
        except Exception as e:
            print(f"Ошибка при получении путей к трекам: {e}")
            return [], []
        finally:
            cursor.close()

    async def get_recommendations(self, user_id: int, top_n: int = 10):
        """
        Получает рекомендации треков на основе коллаборативной фильтрации (возвращает названия и пути).
        """
        recommended_track_ids = await self.get_top_rated_track_ids_by_similar_users(user_id, top_n=top_n)
        recommended_names, recommended_paths = await self.get_track_paths_by_ids(recommended_track_ids)
        return list(zip(recommended_names, recommended_paths))