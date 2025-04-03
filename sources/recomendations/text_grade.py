from sources.postgres.sql_requests import get_text_vector
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_similar_track(target_trackid, vector_name, top_n=10):
    try:
        # Получаем все вектора (теперь там есть trackid, name, song и вектор)
        vectors_dict = get_text_vector(vector_name)
        if not vectors_dict:
            return []

        # Проверяем наличие целевого трека
        target_vector_data = vectors_dict.get(target_trackid)
        if target_vector_data is None or vector_name not in target_vector_data:
            return []

        target_vector = target_vector_data[vector_name]

        # Подготавливаем данные для сравнения
        other_data = []
        for tid, data in vectors_dict.items():
            if tid != target_trackid and vector_name in data and data[vector_name] is not None:
                other_data.append((tid, data[vector_name], data['name'], data['song']))

        if not other_data:
            return []

        # Вычисляем сходство
        target_vector = np.array(target_vector).reshape(1, -1)
        other_vectors = np.array([x[1] for x in other_data])

        similarities = cosine_similarity(target_vector, other_vectors)[0]

        # Сортируем по убыванию сходства
        sorted_indices = np.argsort(similarities)[::-1][:top_n]

        # Формируем результат с name и song
        result = []
        for idx in sorted_indices:
            track_data = other_data[idx]
            result.append({
                'trackid': track_data[0],
                'name': track_data[2],  # название трека
                'song': track_data[3]  # путь к треку
            })

        return result

    except Exception as e:
        print(f"Ошибка при поиске похожих треков: {e}")
        return []


def get_similar_tracks(target_trackid, top_n=10):
    # Получаем похожие треки по двум типам векторов
    tracks1 = get_similar_track(target_trackid, "textvector")
    tracks2 = get_similar_track(target_trackid, "textllmvector")

    # Объединяем результаты
    combined = tracks1 + tracks2

    # Удаляем дубликаты с сохранением порядка
    seen = set()
    unique_tracks = []
    for track in combined:
        track_id = track['trackid']
        if track_id not in seen:
            seen.add(track_id)
            unique_tracks.append(track)

    # Формируем отдельные списки имен и путей
    names = []
    paths = []
    for track in unique_tracks[:top_n]:
        names.append(track['name'])
        paths.append(track['song'])

    return names, paths

if __name__ == "__main__":
    n, m = get_similar_tracks(36)
    print(n)
    print(m)