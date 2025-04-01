import psycopg2
from datetime import date, timedelta
import random
import numpy as np
import os

# --- Конфигурация базы данных ---
DB_NAME = 'music_db1'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'

# --- Папка с аудиофайлами (измените на свой путь) ---
AUDIO_FOLDER = 'audio'

conn = None
cursor = None

try:
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cursor = conn.cursor()
    print("Успешное подключение к базе данных")

    # --- Более осмысленные данные ---
    artists = ["Nirvana", "Radiohead", "Billie Eilish", "Kendrick Lamar", "Tame Impala"]
    genres = ["Grunge", "Alternative Rock", "Pop", "Hip-Hop", "Psychedelic Rock"]
    albums_data = [
        {"artist": "Nirvana", "name": "Nevermind", "year": 1991},
        {"artist": "Nirvana", "name": "In Utero", "year": 1993},
        {"artist": "Radiohead", "name": "OK Computer", "year": 1997},
        {"artist": "Radiohead", "name": "Kid A", "year": 2000},
        {"artist": "Billie Eilish", "name": "When We All Fall Asleep, Where Do We Go?", "year": 2019},
        {"artist": "Billie Eilish", "name": "Happier Than Ever", "year": 2021},
        {"artist": "Kendrick Lamar", "name": "To Pimp a Butterfly", "year": 2015},
        {"artist": "Kendrick Lamar", "name": "DAMN.", "year": 2017},
        {"artist": "Tame Impala", "name": "Lonerism", "year": 2012},
        {"artist": "Tame Impala", "name": "Currents", "year": 2015}
    ]
    tracks_data = [
        {"name": "Smells Like Teen Spirit", "artist": "Nirvana", "album": "Nevermind", "genre": "Grunge", "year": 1991},
        {"name": "Come As You Are", "artist": "Nirvana", "album": "Nevermind", "genre": "Grunge", "year": 1992},
        {"name": "Lithium", "artist": "Nirvana", "album": "Nevermind", "genre": "Grunge", "year": 1992},
        {"name": "Heart-Shaped Box", "artist": "Nirvana", "album": "In Utero", "genre": "Grunge", "year": 1993},
        {"name": "All Apologies", "artist": "Nirvana", "album": "In Utero", "genre": "Grunge", "year": 1993},
        {"name": "Paranoid Android", "artist": "Radiohead", "album": "OK Computer", "genre": "Alternative Rock", "year": 1997},
        {"name": "Karma Police", "artist": "Radiohead", "album": "OK Computer", "genre": "Alternative Rock", "year": 1997},
        {"name": "Creep", "artist": "Radiohead", "album": None, "genre": "Alternative Rock", "year": 1992},  # Single
        {"name": "Everything In Its Right Place", "artist": "Radiohead", "album": "Kid A", "genre": "Alternative Rock", "year": 2000},
        {"name": "Idioteque", "artist": "Radiohead", "album": "Kid A", "genre": "Alternative Rock", "year": 2000},
        {"name": "bad guy", "artist": "Billie Eilish", "album": "When We All Fall Asleep, Where Do We Go?", "genre": "Pop", "year": 2019},
        {"name": "bury a friend", "artist": "Billie Eilish", "album": "When We All Fall Asleep, Where Do We Go?", "genre": "Pop", "year": 2019},
        {"name": "happier than ever", "artist": "Billie Eilish", "album": "Happier Than Ever", "genre": "Pop", "year": 2021},
        {"name": "Therefore I Am", "artist": "Billie Eilish", "album": None, "genre": "Pop", "year": 2020},  # Single
        {"name": "Alright", "artist": "Kendrick Lamar", "album": "To Pimp a Butterfly", "genre": "Hip-Hop", "year": 2015},
        {"name": "King Kunta", "artist": "Kendrick Lamar", "album": "To Pimp a Butterfly", "genre": "Hip-Hop", "year": 2015},
        {"name": "HUMBLE.", "artist": "Kendrick Lamar", "album": "DAMN.", "genre": "Hip-Hop", "year": 2017},
        {"name": "DNA.", "artist": "Kendrick Lamar", "album": "DAMN.", "genre": "Hip-Hop", "year": 2017},
        {"name": "The Less I Know The Better", "artist": "Tame Impala", "album": "Currents", "genre": "Psychedelic Rock", "year": 2015},
        {"name": "Elephant", "artist": "Tame Impala", "album": "Lonerism", "genre": "Psychedelic Rock", "year": 2012},
        {"name": "Feels Like We Only Go Backwards", "artist": "Tame Impala", "album": "Lonerism", "genre": "Psychedelic Rock", "year": 2012},
        {"name": "New Person, Same Old Mistakes", "artist": "Tame Impala", "album": "Currents", "genre": "Psychedelic Rock", "year": 2015},
        {"name": "Smells Like Teen Spirit (Live)", "artist": "Nirvana", "album": "Nevermind", "genre": "Grunge", "year": 1992} # Пример дубликата названия
    ]

    target_user_id = 1868695254
    listening_days = 30
    num_other_users = 5  # Количество дополнительных пользователей для создания

    # --- Генерация случайных векторов признаков ---
    def generate_random_vector(length):
        return np.random.rand(length).astype(np.float32).tolist() # Сначала создаем numpy array, потом преобразуем в список

    def generate_svd_vector(length):
        return np.random.normal(0, 1, length).astype(np.float32).tolist() # Сначала создаем numpy array, потом преобразуем в список

    def generate_emotion_matrix(num_users):
        # Пример: матрица взаимодействия пользователей и треков (случайные -1, 0, 1)
        return [[random.choice([-1, 0, 1]) for _ in range(num_users)] for _ in range(5)] # Пример для 5 пользователей

    # --- Заполнение таблиц ---

    # Пользователи (проверяем, существует ли пользователь)
    user_ids = []
    for i in range(num_other_users):
        user_id = random.randint(1000000000, 2000000000)
        user_ids.append(user_id)
        cursor.execute("SELECT UserId FROM Users WHERE UserId = %s", (user_id,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO Users (UserId) VALUES (%s)", (user_id,))
            conn.commit()
            print(f"Добавлен пользователь с ID {user_id} в таблицу Users")
        else:
            print(f"Пользователь с ID {user_id} уже существует в таблице Users")
    user_ids.append(target_user_id)
    cursor.execute("SELECT UserId FROM Users WHERE UserId = %s", (target_user_id,))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO Users (UserId) VALUES (%s)", (target_user_id,))
        conn.commit()
        print(f"Пользователь с ID {target_user_id} добавлен в таблицу Users")
    else:
        print(f"Пользователь с ID {target_user_id} уже существует в таблице Users")

    print("Таблица Users обновлена")

    # Исполнители
    artist_ids = {}
    for artist_name in artists:
        cursor.execute("SELECT ArtistId FROM Artists WHERE Name = %s", (artist_name,))
        result = cursor.fetchone()
        if result:
            artist_ids[artist_name] = result[0]
        else:
            cursor.execute("INSERT INTO Artists (Name) VALUES (%s) RETURNING ArtistId", (artist_name,))
            artist_result = cursor.fetchone()
            artist_ids[artist_name] = artist_result[0] if artist_result else None
    conn.commit()
    print("Таблица Artists заполнена")

    # Жанры
    genre_ids = {}
    for genre_name in genres:
        cursor.execute("SELECT GenreId FROM Genres WHERE GenreName = %s", (genre_name,))
        result = cursor.fetchone()
        if result:
            genre_ids[genre_name] = result[0]
        else:
            cursor.execute("INSERT INTO Genres (GenreName) VALUES (%s) RETURNING GenreId", (genre_name,))
            genre_result = cursor.fetchone()
            genre_ids[genre_name] = genre_result[0] if genre_result else None
    conn.commit()
    print("Таблица Genres заполнена")

    # Альбомы
    album_ids = {}
    for album_info in albums_data:
        artist_id = artist_ids.get(album_info['artist'])
        if artist_id:
            cursor.execute("SELECT AlbumId FROM Albums WHERE Name = %s", (album_info['name'],))
            result = cursor.fetchone()
            album_id = result[0] if result else None
            if not album_id:
                album_year = date(album_info['year'], 1, 1)
                cursor.execute("INSERT INTO Albums (Name, Year) VALUES (%s, %s) RETURNING AlbumId", (album_info['name'], album_year))
                album_result = cursor.fetchone()
                album_id = album_result[0] if album_result else None
            if album_id:
                album_ids[(album_info['artist'], album_info['name'])] = album_id
                cursor.execute("SELECT 1 FROM AlbumArtists WHERE AlbumId = %s AND ArtistId = %s", (album_id, artist_id))
                if not cursor.fetchone():
                    cursor.execute("INSERT INTO AlbumArtists (AlbumId, ArtistId) VALUES (%s, %s)", (album_id, artist_id))
    conn.commit()
    print("Таблицы Albums и AlbumArtists заполнены")

    # Треки
    track_ids = {}
    num_tracks = len(tracks_data)
    emotion_matrix = generate_emotion_matrix(len(user_ids)) # Генерируем матрицу взаимодействия
    for i, track_info in enumerate(tracks_data):
        artist_id = artist_ids.get(track_info['artist'])
        album_key = (track_info['artist'], track_info['album'])
        album_id = album_ids.get(album_key) if track_info['album'] else None

        if artist_id:
            sql_query = "SELECT TrackId FROM Tracks WHERE Name = %s AND ArtistId = %s"
            params = (track_info['name'], artist_id)

            if album_id is not None:
                sql_query += " AND AlbumId = %s"
                params += (album_id,)
            else:
                sql_query += " AND AlbumId IS NULL"

            cursor.execute(sql_query, params)
            result = cursor.fetchone()
            track_id = result[0] if result else None

            if not track_id:
                track_year = date(track_info['year'], 1, 1)
                # Формируем ссылку на песню (предполагая, что файлы лежат в audio и называются как Name с расширением .mp3)
                song_link = os.path.join(AUDIO_FOLDER, track_info['name'].replace(' ', '_') + '.mp3')
                features_vector = generate_random_vector(128) # Пример размера вектора признаков
                svd_features_vector = generate_svd_vector(50) # Пример размера SVD-вектора
                emotion_vector_str = str(emotion_matrix[i % 5]) # Пример циклического назначения эмоций
                cursor.execute(
                    "INSERT INTO Tracks (Name, ArtistId, AlbumId, Year, Song, Features, SVDFeatures, EmotionVector) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING TrackId",
                    (track_info['name'], artist_id, album_id, track_year, song_link, features_vector, svd_features_vector, emotion_vector_str)
                )
                track_result = cursor.fetchone()
                track_id = track_result[0] if track_result else None
            elif track_id:
                # Если трек уже существует, мы можем обновить поля Features и SVDFeatures тестовыми данными
                features_vector = generate_random_vector(128)
                svd_features_vector = generate_svd_vector(50)
                cursor.execute(
                    "UPDATE Tracks SET Features = %s, SVDFeatures = %s WHERE TrackId = %s",
                    (features_vector, svd_features_vector, track_id)
                )

            if track_id:
                track_ids[track_info['name']] = track_id
                genre_id = genre_ids.get(track_info['genre'])
                if genre_id:
                    cursor.execute("SELECT 1 FROM TrackGenres WHERE TrackId = %s AND GenreId = %s", (track_id, genre_id))
                    if not cursor.fetchone():
                        cursor.execute("INSERT INTO TrackGenres (TrackId, GenreId) VALUES (%s, %s)", (track_id, genre_id))
    conn.commit()
    print("Таблицы Tracks и TrackGenres заполнены (с Features, SVDFeatures и EmotionVector)")

    # История прослушиваний для нескольких пользователей
    all_user_ids = user_ids
    for user_index, user_id in enumerate(all_user_ids):
        start_date = date.today() - timedelta(days=listening_days - 1)
        random.shuffle(tracks_data) # Перемешиваем треки для каждого пользователя
        for i, track_info in enumerate(tracks_data[:random.randint(10, len(tracks_data))]): # Каждый пользователь слушает разное кол-во треков
            track_id = track_ids.get(track_info['name'])
            if track_id:
                listening_date = start_date + timedelta(days=i % listening_days)
                rating = random.choice([-1, 0, 1]) # Случайная оценка песни пользователем
                cursor.execute("INSERT INTO History (UserId, TrackId, ListeningDate, rating) VALUES (%s, %s, %s, %s)", (user_id, track_id, listening_date, rating))
        conn.commit()
        print(f"История прослушиваний с рейтингами для пользователя с ID {user_id} заполнена")

    # Плейлист "Избранное" для конкретного пользователя
    cursor.execute("SELECT PlaylistId FROM Playlists WHERE Name = 'Избранное' AND UserId = %s", (target_user_id,))
    playlist_result = cursor.fetchone()
    playlist_id = playlist_result[0] if playlist_result else None
    if not playlist_id:
        cursor.execute("INSERT INTO Playlists (Name, UserId) VALUES ('Избранное', %s) RETURNING PlaylistId", (target_user_id,))
        playlist_creation_result = cursor.fetchone()
        playlist_id = playlist_creation_result[0] if playlist_creation_result else None

    if playlist_id:
        specific_tracks_to_add = [
            "Smells Like Teen Spirit",
            "Karma Police",
            "bad guy",
            "HUMBLE.",
            "Elephant"
        ]
        for track_name in specific_tracks_to_add:
            track_id = track_ids.get(track_name)
            if track_id:
                cursor.execute("SELECT 1 FROM PlaylistTracks WHERE PlaylistId = %s AND TrackId = %s", (playlist_id, track_id))
                if not cursor.fetchone():
                    cursor.execute("INSERT INTO PlaylistTracks (PlaylistId, TrackId) VALUES (%s, %s)", (playlist_id, track_id))
    conn.commit()
    print(f"Плейлист 'Избранное' для пользователя с ID {target_user_id} заполнен")

    print("Заполнение базы данных завершено.")

except psycopg2.Error as e:
    print(f"Ошибка при работе с PostgreSQL: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        print("Соединение с базой данных закрыто")