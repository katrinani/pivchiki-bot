import os
import tensorflow as tf
import numpy as np
import tensorflow_hub as hub
import librosa
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

from sources.postgres.sql_requests import get_features

# Загрузка модели VGGish
os.environ['TFHUB_CACHE_DIR'] = 'tfhub_cache'

model = hub.load("https://tfhub.dev/google/vggish/1")


def to_svd(features: list[float]):
    svd = TruncatedSVD(n_components=3)
    svd_features = svd.fit_transform([features])[0].tolist()
    return svd_features


# Функция для извлечения признаков из аудиофрагмента
def extract_features(audio_path) -> np.ndarray:
    audio, sr = librosa.load(audio_path, sr=16000) # Загрузка аудио
    features = model(audio) # Извлечение признаков с помощью VGGish
    features = np.mean(features, axis=0) # Усреднение признаков по времени

    return features


# Функция для поиска наиболее похожей песни
def find_most_similar_song(input_audio_path: str):
    input_features = extract_features(input_audio_path)

    # Теперь словарь содержит кортежи (features, name) для каждой песни
    database_features: dict[str, tuple[list[float], str]] = get_features()

    max_similarity = -1
    best_song = None
    best_name = None  # Добавляем переменную для хранения имени

    for song_name, (song_features, name) in database_features.items():
        # Вычисление косинусного сходства
        similarity = cosine_similarity([input_features], [song_features])[0][0]

        if similarity > max_similarity:
            max_similarity = similarity
            best_song = song_name
            best_name = name  # Сохраняем соответствующее имя

    # Возвращаем название песни, имя и значение сходства
    return best_song, best_name, max_similarity


if __name__ == "__main__":
    os.makedirs("sources/model", exist_ok=True)
    model_url = "https://tfhub.dev/google/vggish/1"
    model = hub.load(model_url)
    tf.saved_model.save(model, "sources/model")