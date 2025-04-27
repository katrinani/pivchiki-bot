from sources.postgres import config
from sources.postgres.sql_requests import create_user

users = [
    424379637,
    583291746,
    912475368,
    647823915,
    381956274,
    729384561,
    856173492,
    493827165,
    218745639,
    675912483
]




def main():
    import psycopg2
    import random

    # Подключение к базе данных
    conn = psycopg2.connect(
        host=config.config_db["host"],
        database=config.config_db["dbname"],
        user=config.config_db["user"],
        password=config.config_db["password"]
    )

    cursor = conn.cursor()

    # Получаем список всех userid из таблицы пользователей
    cursor.execute("SELECT userid FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]

    # Получаем список всех trackid из таблицы треков
    cursor.execute("SELECT trackid FROM tracks")
    track_ids = [row[0] for row in cursor.fetchall()]

    # Заполняем таблицу usertrackratings
    for user_id in user_ids:
        # Выбираем случайное количество песен от 10 до 20
        num_ratings = random.randint(10, 20)
        # Выбираем случайные треки для оценки
        selected_tracks = random.sample(track_ids, num_ratings)

        for track_id in selected_tracks:
            # Генерируем случайную оценку (1 или -1)
            rating = random.choice([1, -1])
            # Вставляем данные в таблицу
            cursor.execute(
                "INSERT INTO usertrackratings (trackid, userid, rating) VALUES (%s, %s, %s)",
                (track_id, user_id, rating)
            )

    # Фиксируем изменения и закрываем соединение
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    for user in users:
        create_user(user)
    main()