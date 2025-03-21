import numpy as np
import tensorflow_hub as hub
import librosa
from sklearn.metrics.pairwise import cosine_similarity

# Загрузка предобученной модели VGGish
model = hub.load('https://tfhub.dev/google/vggish/1')

# Функция для извлечения признаков из аудиофрагмента
def extract_features(audio_path):

    audio, sr = librosa.load(audio_path, sr=16000) # Загрузка аудио
    features = model(audio) # Извлечение признаков с помощью VGGish
    features = np.mean(features, axis=0) # Усреднение признаков по времени

    return features


# Функция для поиска наиболее похожей песни
def find_most_similar_song(input_audio_path: str):
    # Извлечение признаков для голосового сообщения
    input_features = extract_features(input_audio_path)

    # TODO запроос к бд за свойствами каждой песни
    database_features: dict[str, list[float]] = {"song": [0.22, 0.33]}

    max_similarity = -1
    best_song = None

    for song_name, song_features in database_features.items():
        # Вычисление косинусного сходства
        similarity = cosine_similarity([input_features], [song_features])[0][0]

        if similarity > max_similarity:
            max_similarity = similarity # Сходство
            best_song = song_name # Наиболее похожая песня

    return best_song, max_similarity
