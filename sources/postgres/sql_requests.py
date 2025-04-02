import psycopg2
# pip install psycopg2-binary

from .config import config_db


conn = psycopg2.connect(
    dbname="music_db1",
    user="postgres",
    password="postgres",
    host="localhost"
)

def create_user(user_id: int):
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN;")

        # 1. Создаем пользователя
        cursor.execute(
            "INSERT INTO Users (UserId) VALUES (%s);",
            (user_id,)
        )
        # 2. Создаем плейлист "Избранное" для этого пользователя
        cursor.execute(
            "INSERT INTO Playlists (Name, UserId) VALUES ('Избранное', %s);",
            (user_id,)
        )

        conn.commit()
        return True

    except Exception as e:
        if 'duplicate key value violates unique constraint "users_pkey"' in e.args[0]:
            conn.rollback()
            print("Успешная авторизация")
            return True

        conn.rollback()
        print(f"Error creating user: {e}")
        return False

    finally:
        cursor.close()


def get_features():
    cursor = conn.cursor()
    sql = """
    SELECT Name, Features FROM Tracks WHERE Features IS NOT NULL;
    """
    cursor.execute(sql)
    features_dict = {row[0]: row[1] for row in cursor.fetchall()}
    cursor.close()
    return features_dict


def save_search_history(user_id: int, track_name: str):
    """Save user search history to database"""
    try:
        with conn.cursor() as cursor:
            # Insert search history record
            cursor.execute("""
                INSERT INTO history (
                    userid, 
                    trackname,
                    listeningdate
                )
                VALUES (
                    %s,
                    %s,
                    NOW()
                )
            """, (
                user_id,
                track_name
            ))

            conn.commit()

    except Exception as e:
        print(f"Error saving search history: {e}")
        conn.rollback()
        raise

def get_history(user_id: int) -> list[dict[str, str]]:
    """Get user search history from database"""
    try:
        with conn.cursor() as cursor:
            # Get search history records
            cursor.execute("""
                            SELECT 
                                trackname,
                                listeningdate
                            FROM 
                                history
                            WHERE 
                                userid = %s
                            ORDER BY 
                                listeningdate DESC
                        """, (user_id,))

            history = []
            for track_name, listening_date in cursor.fetchall():
                # Двойная проверка на случай, если проверка в SQL не сработала
                if listening_date is None:
                    continue

                history.append({
                    "date": listening_date.strftime("%d.%m.%Y"),
                    "song": track_name if track_name else "Без названия"
                })

            return history

    except Exception as e:
        print(f"Error fetching search history: {e}")
        raise


# TODO вытащить ссылки на песни
def get_all_playlists(id_user: int) -> dict[str, list[str] | list]:
    """
    Получение плейлистов и песен в нем конкретного пользователя
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.Name, t.Song
        FROM Playlists p
        LEFT JOIN PlaylistTracks pt ON p.PlaylistId = pt.PlaylistId
        LEFT JOIN Tracks t ON pt.TrackId = t.TrackId
        WHERE p.UserId = %s
        ORDER BY p.Name, t.Song
    """, (id_user,))

    playlists = {}
    for row in cursor.fetchall():
        playlist_name = row[0]
        song = row[1]

        if playlist_name not in playlists:
            playlists[playlist_name] = []

        if song:
            playlists[playlist_name].append(song)

    cursor.close()
    return playlists


async def save_mp3(path: str, name: str, features: list[float], svd_features: list[float]):
    query = """
        INSERT INTO Tracks (Song, Name, Features, SVDFeatures)
        VALUES (%s, %s, %s, %s)
        RETURNING TrackId;
    """

    cursor = conn.cursor()
    try:
        cursor.execute(query, (path, name, features, svd_features))

        if cursor.rowcount != 1:
            return False  # или можно вызвать исключение

        # Получаем TrackId из результата запроса
        track_id = cursor.fetchone()[0]

        conn.commit()
        return track_id, True

    except Exception as e:
        conn.rollback()
        print(f"Ошибка при сохранении трека: {e}")
        return 0, False  # или можно вызвать исключение

    finally:
        cursor.close()


def rename_playlist(playlist_name: str, new_name: str, user_id: int):
    """
    Переименовывает плейлист конкретного пользователя
    :return: True если успешно, False если ошибка или плейлист не найден
    """
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN;")
        # Обновляем только плейлист с указанным именем и user_id
        cursor.execute(
            "UPDATE Playlists SET Name = %s WHERE Name = %s AND UserId = %s",
            (new_name, playlist_name, user_id)
        )

        if cursor.rowcount != 1:  # Проверяем что обновили именно 1 запись
            return False

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Error renaming playlist: {e}")
        return False
    finally:
        cursor.close()


def create_playlist(user_id: int, playlist_name: str):
    """
    Создает новый плейлист
    :return: True если успешно, False если ошибка
    """
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN;")

        # Создаем плейлист и возвращаем его ID
        cursor.execute(
            "INSERT INTO Playlists (Name, UserId) VALUES (%s, %s) RETURNING playlistid;",
            (playlist_name, user_id)
        )

        cursor.fetchone()
        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Error creating playlist: {e}")
        return False
    finally:
        cursor.close()


def delete_playlist(playlist_name: str, user_id: int):
    """
    Удаляет плейлист конкретного пользователя по названию (каскадно удалит все связи с треками)
    :return: True если успешно, False если ошибка или плейлист не найден
    """
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN;")
        # Удаляем только плейлист с указанным именем и user_id
        cursor.execute(
            "DELETE FROM Playlists WHERE Name = %s AND UserId = %s",
            (playlist_name, user_id)
        )

        if cursor.rowcount != 1:  # Проверяем что удалили именно 1 запись
            return False

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Error deleting playlist: {e}")
        return False
    finally:
        cursor.close()


def remove_song_from_playlist(playlist_name: str, user_id: int, song_name: str):
    """
    Удаляет песню по названию из плейлиста пользователя
    :return: True если успешно, False если ошибка или песня/плейлист не найдены
    """
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN;")

        # 1. Находим ID плейлиста по имени и пользователю
        cursor.execute(
            "SELECT PlaylistId FROM Playlists WHERE Name = %s AND UserId = %s",
            (playlist_name, user_id)
        )
        playlist = cursor.fetchone()

        if not playlist:
            return False  # Плейлист не найден

        playlist_id = playlist[0]

        # 2. Находим ID трека по названию песни
        cursor.execute(
            "SELECT TrackId FROM Tracks WHERE Name = %s",
            (song_name,)
        )
        track = cursor.fetchone()

        if not track:
            return False  # Трек не найден

        track_id = track[0]

        # 3. Удаляем связь между плейлистом и треком
        cursor.execute(
            "DELETE FROM PlaylistTracks WHERE PlaylistId = %s AND TrackId = %s",
            (playlist_id, track_id)
        )

        if cursor.rowcount != 1:
            return False  # Связь не найдена

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Error removing song from playlist: {e}")
        return False
    finally:
        cursor.close()


def rebase_song_from_playlist(song_name: str, playlist_to_name: str = None, playlist_from_name: str = None):
    """
    Функция для добавления песни в плейлист (если задан playlist_to_name)
    или переноса песни из одного плейлиста в другой (если заданы playlist_to_name, playlist_from_name)
    по названиям песни и плейлистов.
    :return: True/False в зависимости от того как прошла операция
    """
    if not playlist_to_name:
        return False

    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN;")

        # Получаем ID песни по названию
        cursor.execute("SELECT TrackId FROM Tracks WHERE Name = %s", (song_name,))
        song_result = cursor.fetchone()
        if not song_result:
            return False
        id_song = song_result[0]

        # Получаем ID целевого плейлиста по названию
        cursor.execute("SELECT PlaylistId FROM Playlists WHERE Name = %s", (playlist_to_name,))
        playlist_to_result = cursor.fetchone()
        if not playlist_to_result:
            return False
        id_playlist_to = playlist_to_result[0]

        if playlist_from_name:
            # Получаем ID исходного плейлиста по названию
            cursor.execute("SELECT PlaylistId FROM Playlists WHERE Name = %s", (playlist_from_name,))
            playlist_from_result = cursor.fetchone()
            if not playlist_from_result:
                return False
            id_playlist_from = playlist_from_result[0]

            # Проверяем, есть ли песня в исходном плейлисте
            cursor.execute(
                "SELECT 1 FROM PlaylistTracks WHERE TrackId = %s AND PlaylistId = %s",
                (id_song, id_playlist_from))
            if not cursor.fetchone():
                return False

            # Удаление из исходного плейлиста
            cursor.execute(
                "DELETE FROM PlaylistTracks WHERE TrackId = %s AND PlaylistId = %s",
                (id_song, id_playlist_from))

        # Добавление в целевой плейлист
        cursor.execute(
            """INSERT INTO PlaylistTracks (PlaylistId, TrackId)
               VALUES (%s, %s)
               ON CONFLICT (PlaylistId, TrackId) DO NOTHING""",
            (id_playlist_to, id_song))

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Error in rebase_song_from_playlist: {e}")
        return False
    finally:
        cursor.close()

def save_song_to_db(title, file_path, lyrics, language, text_vector, text_llm_vector, features):
    """Save song information to tracks and artists tables"""
    try:
        with conn.cursor() as cursor:

            cursor.execute("""
                INSERT INTO tracks (
                    song,
                    trackid,
                    name,
                    lyrics, 
                    language,
                    textvector,
                    textllmvector,
                    features
                )
                VALUES (%s, DEFAULT, %s, %s, %s, %s, %s, %s)
                RETURNING trackid
            """, (
                file_path,
                title,
                lyrics,
                language,
                text_vector,
                text_llm_vector,
                features
            ))


            conn.commit()

    except Exception as e:
        print(f"Ошибка при сохранении в базу данных: {e}")
        conn.rollback()
        raise
"""
-- Таблица пользователей
CREATE TABLE Users (
    UserId SERIAL PRIMARY KEY
);

-- Таблица исполнителей
CREATE TABLE Artists (
    ArtistId SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

-- Таблица жанров
CREATE TABLE Genres (
    GenreId SERIAL PRIMARY KEY,
    GenreName VARCHAR(255) NOT NULL
);

-- Таблица альбомов
CREATE TABLE Albums (
    AlbumId SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Year DATE
);

-- Таблица треков (добавлено поле Lyrics)
CREATE TABLE Tracks (
    TrackId SERIAL PRIMARY KEY,
    Song TEXT,  -- Хранит ссылку на песню
    Lyrics TEXT,	-- Добавлено поле для хранения текста песни
	Name VARCHAR(255),
    ArtistId INT,
	Name VARCHAR(255),
    AlbumId INT,
    Year DATE,
    Language TEXT,
    Features REAL[],
    SVDFeatures REAL[],
	EmotionVector REAL[],
    PhysicalSimilarTracksIds INT[],
    TextSimilarTracksIds INT[],
    CollaborationSimilarTracksIds INT[],
    FOREIGN KEY (ArtistId) REFERENCES Artists(ArtistId) ON DELETE CASCADE,
    FOREIGN KEY (AlbumId) REFERENCES Albums(AlbumId) ON DELETE CASCADE
);

-- Таблица плейлистов
CREATE TABLE Playlists (
    PlaylistId SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    UserId INT,
    FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE
);

-- Таблица истории прослушиваний
CREATE TABLE History (
    HistoryId SERIAL PRIMARY KEY,
    UserId INT,
    TrackId INT,
	rating INT DEFAULT 0,
    ListeningDate DATE,
    FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
    FOREIGN KEY (TrackId) REFERENCES Tracks(TrackId) ON DELETE CASCADE
);

-- Таблица связей треков и жанров
CREATE TABLE TrackGenres (
    TrackId INT,
    GenreId INT,
    PRIMARY KEY (TrackId, GenreId),
    FOREIGN KEY (TrackId) REFERENCES Tracks(TrackId) ON DELETE CASCADE,
    FOREIGN KEY (GenreId) REFERENCES Genres(GenreId) ON DELETE CASCADE
);

-- Таблица связей альбомов и жанров
CREATE TABLE AlbumGenres (
    AlbumId INT,
    GenreId INT,
    PRIMARY KEY (AlbumId, GenreId),
    FOREIGN KEY (AlbumId) REFERENCES Albums(AlbumId) ON DELETE CASCADE,
    FOREIGN KEY (GenreId) REFERENCES Genres(GenreId) ON DELETE CASCADE
);

-- Таблица связей артистов и жанров
CREATE TABLE ArtistGenres (
    ArtistId INT,
    GenreId INT,
    PRIMARY KEY (ArtistId, GenreId),
    FOREIGN KEY (ArtistId) REFERENCES Artists(ArtistId) ON DELETE CASCADE,
    FOREIGN KEY (GenreId) REFERENCES Genres(GenreId) ON DELETE CASCADE
);

-- Таблица связей альбомов и артистов
CREATE TABLE AlbumArtists (
    AlbumId INT,
    ArtistId INT,
    PRIMARY KEY (AlbumId, ArtistId),
    FOREIGN KEY (AlbumId) REFERENCES Albums(AlbumId) ON DELETE CASCADE,
    FOREIGN KEY (ArtistId) REFERENCES Artists(ArtistId) ON DELETE CASCADE
);

-- Таблица связей плейлистов и треков
CREATE TABLE PlaylistTracks (
    PlaylistId INT,
    TrackId INT,
    PRIMARY KEY (PlaylistId, TrackId),
    FOREIGN KEY (PlaylistId) REFERENCES Playlists(PlaylistId) ON DELETE CASCADE,
    FOREIGN KEY (TrackId) REFERENCES Tracks(TrackId) ON DELETE CASCADE
);

-- Таблица связей пользователей и альбомов
CREATE TABLE UserAlbums (
    UserId INT,
    AlbumId INT,
    PRIMARY KEY (UserId, AlbumId),
    FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
    FOREIGN KEY (AlbumId) REFERENCES Albums(AlbumId) ON DELETE CASCADE
);

-- Таблица связей пользователей и любимых исполнителей
CREATE TABLE UserFavoriteArtists (
    UserId INT,
    ArtistId INT,
    PRIMARY KEY (UserId, ArtistId),
    FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
    FOREIGN KEY (ArtistId) REFERENCES Artists(ArtistId) ON DELETE CASCADE
);

-- Таблица связей пользователей и истории прослушиваний
CREATE TABLE UserHistory (
    UserId INT,
    HistoryId INT,
    PRIMARY KEY (UserId, HistoryId),
    FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
    FOREIGN KEY (HistoryId) REFERENCES History(HistoryId) ON DELETE CASCADE
);

"""