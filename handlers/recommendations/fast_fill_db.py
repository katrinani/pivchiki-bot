import psycopg2
import os

# --- Конфигурация базы данных ---
DB_NAME = 'music_db1'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'

# --- Папка с аудиофайлами (относительно текущего скрипта) ---
AUDIO_FOLDER = '../../audio'

conn = None
cursor = None

try:
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cursor = conn.cursor()
    print("Успешное подключение к базе данных")

    # --- Получаем все TrackId и Name из таблицы Tracks ---
    cursor.execute("SELECT TrackId, Name FROM Tracks")
    tracks = cursor.fetchall()

    updated_count = 0
    for track_id, track_name in tracks:
        # Формируем относительный путь к MP3 файлу
        song_filename = track_name + '.mp3'
        song_path = os.path.join(AUDIO_FOLDER, song_filename)

        # Проверяем, существует ли файл (опционально, но рекомендуется)
        if os.path.exists(song_path):
            # --- Обновляем поле Song в таблице Tracks ---
            update_query = "UPDATE Tracks SET Song = %s WHERE TrackId = %s"
            cursor.execute(update_query, (song_path, track_id))
            updated_count += 1
            print(f"Обновлен путь для трека ID {track_id}: {song_path}")
        else:
            print(f"Аудиофайл не найден для трека ID {track_id} ('{track_name}'): {song_path}")

    # --- Сохраняем изменения ---
    conn.commit()
    print(f"Обновлено поле Song для {updated_count} треков.")

except psycopg2.Error as e:
    print(f"Ошибка при работе с PostgreSQL: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        print("Соединение с базой данных закрыто")