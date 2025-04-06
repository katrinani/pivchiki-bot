import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics import mean_squared_error
from math import sqrt
import pandas as pd


data = {
    'userId': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
               3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
               5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
               6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
               7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
               8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
               9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
               10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    'itemId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10,
    'rating': [0, 4, 0, 2, 1, 0, 5, 4, 0, 2,   # userId 1
               0, 5, 4, 3, 2, 1, 0, 5, 4, 3,   # userId 2
               2, 1, 0, 5, 4, 3, 2, 1, 0, 5,   # userId 3
               4, 3, 2, 1, 0, 5, 4, 3, 2, 1,   # userId 4
               0, 5, 4, 3, 2, 1, 0, 5, 4, 3,   # userId 5
               2, 1, 0, 5, 4, 3, 2, 1, 0, 5,   # userId 6
               4, 3, 2, 1, 0, 5, 4, 3, 2, 1,   # userId 7
               0, 5, 4, 3, 2, 1, 0, 5, 4, 3,   # userId 8
               2, 1, 0, 5, 4, 3, 2, 1, 0, 5,   # userId 9
               4, 3, 2, 1, 0, 5, 4, 3, 2, 1]   # userId 10
}

df = pd.DataFrame(data)

n_users = df['userId'].unique().shape[0]
n_items = df['itemId'].unique().shape[0]

input_list = df['itemId'].unique()


def scale_item_id(input_id):
    return np.where(input_list == input_id)[0][0] + 1

df['itemId'] = df['itemId'].apply(scale_item_id)


train_data, test_data = train_test_split(df, test_size=0.20)

# Создаем две user-item матрицы – для обучения и для теста
train_data_matrix = np.zeros((n_users, n_items))
for line in train_data.itertuples():
    train_data_matrix[line[1] - 1, line[2] - 1] = line[3]

test_data_matrix = np.zeros((n_users, n_items))
for line in test_data.itertuples():
    test_data_matrix[line[1] - 1, line[2] - 1] = line[3]

# Вычисляем сходство пользователей
user_similarity = pairwise_distances(train_data_matrix, metric='cosine')

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

# Получаем предсказания
user_prediction = predict(train_data_matrix, user_similarity, 'item')

# Для оценки качества предсказания (RMSE)
def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))

# Функция для получения рекомендаций
def get_recommendations(user_id, user_prediction, original_df, n_recommendations):
    user_idx = user_id - 1
    user_ratings = user_prediction[user_idx]

    # Оцененные песни
    rated_movies = original_df[(original_df['userId'] == user_id) & ((original_df['rating'] > 0)) ]['itemId'].values

    # Исключаем прослушенные
    recommendations = []
    for movie_id, predicted_rating in enumerate(user_ratings, start=1):
        if movie_id not in rated_movies:
            recommendations.append((movie_id, predicted_rating))

    # Сортируем рекомендации в порядке убывания
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Выбираем первые n_recommendations песен
    return recommendations[:n_recommendations]

# Получаем рекомендации для пользователя
print(get_recommendations(1, user_prediction, df, 10))
