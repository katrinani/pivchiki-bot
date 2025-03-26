import psycopg2

from config import config_db

conn = psycopg2.connect(
    dbname=config_db["dbname"],
    user=config_db["user"],
    password=config_db["password"],
    host=config_db["host"]
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
        conn.rollback()
        print(f"Error creating user: {e}")
        return False

    finally:
        cursor.close()


def save_search_history(user_id: int, track_name: str):
    cursor = conn.cursor()
    sql = """
    INSERT INTO History (UserId, TrackId, ListeningDate) VALUES (%d, (SELECT TrackId FROM Tracks WHERE Song = %s), NOW())
    """
    cursor.execute(sql, (user_id, track_name, ))
    conn.commit()
    cursor.close()


def get_history(user_id: int) ->  list[dict[str, str]]:
    cursor = conn.cursor()
    sql = """
    SELECT h.ListeningDate, t.Song, a.Name
    FROM History h
    JOIN Tracks t ON h.TrackId = t.TrackId
    JOIN Artists a ON t.ArtistId = a.ArtistId
    WHERE h.UserId = %s
    ORDER BY h.ListeningDate DESC
    """
    cursor.execute(sql, (user_id,))

    history = []
    for record in cursor.fetchall():
        history.append({
            "date": record[0].strftime("%d.%m.%Y"),  # Форматированная дата
            "song": record[1],  # Название песни
            "artist": record[2]  # Имя исполнителя
        })

    cursor.close()
    """ history
    [
    {"date": "15.05.2023", "song": "Bohemian Rhapsody", "artist": "Queen"},
    {"date": "14.05.2023", "song": "Imagine", "artist": "John Lennon"}
    ]
    """
    return history


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


# TODO добавление mp3 в бд

def rename_playlist(playlist_id: int, new_name: str):
    """
    Переименовывает плейлист
    :return: True если успешно, False если ошибка
    """
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN;")
        cursor.execute(
            "UPDATE Playlists SET Name = %s WHERE PlaylistId = %s",
            (new_name, playlist_id)
        )

        if cursor.rowcount != 1: # Проверяем что обновили именно 1 запись
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
            "INSERT INTO Playlists (Name, UserId) VALUES (%s, %s)",
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


def delete_playlist(playlist_id: int):
    """
    Удаляет плейлист (каскадно удалит все связи с треками)
    :return: True если успешно, False если ошибка
    """
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN;")
        cursor.execute(
            "DELETE FROM Playlists WHERE PlaylistId = %s",
            (playlist_id,)
        )
        if cursor.rowcount != 1:
            return False

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Error deleting playlist: {e}")
        return False
    finally:
        cursor.close()


def remove_song_from_playlist(track_id: int, playlist_id: int):
    """
    Удаляет трек из указанного плейлиста
    :return: True если удаление успешно, False если ошибка
    """
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN;")

        # Проверяем существование связи перед удалением
        cursor.execute(
            "SELECT 1 FROM PlaylistTracks WHERE TrackId = %s AND PlaylistId = %s",
            (track_id, playlist_id)
        )
        if not cursor.fetchone():
            return False  # Связи не существует

        # Удаляем трек из плейлиста
        cursor.execute(
            "DELETE FROM PlaylistTracks WHERE TrackId = %s AND PlaylistId = %s",
            (track_id, playlist_id)
        )

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Error removing song from playlist: {e}")
        return False
    finally:
        cursor.close()


def rebase_song_from_playlist(id_song: int, id_playlist_to: int = None, id_playlist_from: int = None):
    """
    Функция для добавления песни в плейлист(если задан id_playlist_to)
    или переноса песни из одного плейлиста в другой (если заданы id_playlist_to, id_playlist_from)
    :return: True/False в зависимости от того как прошла операция
    """
    if not id_playlist_to:
        return False

    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN;")

        cursor.execute("SELECT 1 FROM Tracks WHERE TrackId = %s", (id_song,))
        if not cursor.fetchone():
            return False
        cursor.execute("SELECT 1 FROM Playlists WHERE PlaylistId = %s", (id_playlist_to,))
        if not cursor.fetchone():
            return False


        if id_playlist_from:
            cursor.execute("SELECT 1 FROM Playlists WHERE PlaylistId = %s", (id_playlist_from,))
            if not cursor.fetchone():
                return False
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
