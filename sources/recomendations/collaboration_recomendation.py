import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import pairwise_distances
import pandas as pd
import psycopg2
from sources.postgres import config
from sources.postgres.sql_requests import create_user_item_table


# Функция предсказания
def predict(ratings, similarity, type):
    if type == 'user':
      mean_user_rating = ratings.mean(axis=1)
      ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
      pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'item':
      mean_item_rating = ratings.mean(axis=0)
      ratings_diff = (ratings - mean_item_rating[np.newaxis, :])
      pred = mean_item_rating[np.newaxis, :] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=0)]).T
    return pred



def main_get_recommendations(userid: int):
    conn = psycopg2.connect(
        host=config.config_db["host"],
        database=config.config_db["dbname"],
        user=config.config_db["user"],
        password=config.config_db["password"]
    )

    # Извлечение данных из таблицы
    create_user_item_table()
    query = "SELECT * FROM crosstab_result"
    df = pd.read_sql_query(query, conn)

    # Закрытие соединения
    conn.close()

    # Подготовка данных
    n_users = df['userid'].unique().shape[0]  # Количество уникальных пользователей
    trackid_columns = [col for col in df.columns if col.startswith('trackid')]  # Список столбцов trackid
    n_items = len(trackid_columns)  # Количество уникальных треков

    # Преобразование DataFrame в user-item матрицу
    def create_user_item_matrix(df):
        user_item_matrix = np.zeros((n_users, n_items))
        for i, userid in enumerate(df['userid'].unique()):
            user_data = df[df['userid'] == userid]
            user_item_matrix[i] = user_data[trackid_columns].values.flatten()
        return user_item_matrix

    # Создание user-item матрицы
    user_item_matrix = create_user_item_matrix(df)

    # Разделение данных на обучающую и тестовую выборки
    train_data, test_data = train_test_split(user_item_matrix, test_size=0.20)


    # Вычисляем сходство пользователей
    user_similarity = pairwise_distances(train_data, metric='cosine')

    # Получаем предсказания
    user_prediction = predict(train_data, user_similarity, 'user')

    def get_recommendations(user_id, user_prediction, original_df, n_recommendations=5):
        # Получаем индекс пользователя
        user_idx = original_df['userid'].unique().tolist().index(user_id)
        # Получаем предсказанные оценки для пользователя
        user_ratings = user_prediction[user_idx]

        # Получаем список треков, которые пользователь уже оценил (значение 1 или -1)
        rated_tracks = []
        for col in original_df.columns:
            if col.startswith('trackid'):
                if original_df.loc[original_df['userid'] == user_id, col].values[0] != 0:
                    rated_tracks.append(col)

        # Формируем рекомендации, исключая уже оцененные треки
        recommendations = []
        for track_idx, predicted_rating in enumerate(user_ratings):
            track_id = original_df.columns[track_idx + 1]  # Пропускаем столбец 'userid'
            if track_id not in rated_tracks:
                recommendations.append((track_id, predicted_rating))

        # Сортируем рекомендации в порядке убывания предсказанной оценки
        recommendations.sort(key=lambda x: x[1], reverse=True)

        # Возвращаем топ-n рекомендаций
        return recommendations[:n_recommendations]

    # Получаем рекомендации для пользователя
    return get_recommendations(userid, user_prediction, df)



if __name__ == "__main__":
    main_get_recommendations(424379637)