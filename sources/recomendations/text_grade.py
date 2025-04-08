from sources.postgres.sql_requests import get_text_vector
from sources.postgres.sql_requests import get_best_tracks
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def get_similar_track(target_trackid, vector_name, top_n=10):
    try:
        # Получаем все вектора
        vectors_dict = get_text_vector(vector_name)
        if not vectors_dict:
            return []

        # Проверяем наличие целевого трека
        target_vector_data = vectors_dict.get(target_trackid)
        if target_vector_data is None or vector_name not in target_vector_data:
            return []

        target_vector = target_vector_data[vector_name]

        # Подготавливаем данные для сравнения и находим максимальную длину вектора
        other_data = []
        max_length = len(target_vector) if target_vector is not None else 0

        for tid, data in vectors_dict.items():
            if tid != target_trackid and vector_name in data and data[vector_name] is not None:
                other_data.append((tid, data[vector_name], data['name'], data['song']))
                if len(data[vector_name]) > max_length:
                    max_length = len(data[vector_name])

        if not other_data:
            return []

        # Функция для дополнения вектора нулями до нужной длины
        def pad_vector(vec, length):
            if vec is None:
                return np.zeros(length)
            if len(vec) >= length:
                return np.array(vec[:length])
            return np.pad(vec, (0, length - len(vec)), mode='constant')

        # Дополняем все вектора до одинаковой длины
        padded_target = pad_vector(target_vector, max_length).reshape(1, -1)
        padded_others = [pad_vector(x[1], max_length) for x in other_data]

        # Вычисляем сходство
        other_vectors = np.array(padded_others)
        similarities = cosine_similarity(padded_target, other_vectors)[0]

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


def get_similar_tracks(track_ids, top_n=10):
    print(track_ids)
    all_tracks = []
    for track_id in track_ids:
        # Получаем первый уникальный трек из textvector
        tracks1 = get_similar_track(track_id, "textvector")
        for track in tracks1:
            if track not in all_tracks and track['trackid'] not in track_ids:
                all_tracks.append(track)
                break
        # Получаем первый уникальный трек из textllmvector
        tracks2 = get_similar_track(track_id, "textllmvector")
        for track in tracks2:
            if track not in all_tracks and track['trackid'] not in track_ids:
                all_tracks.append(track)
                break

    # Формируем отдельные списки имен и путей
    names = []
    paths = []
    for track in all_tracks[:top_n]:
        print(track['trackid'])
        names.append(track['name'])
        paths.append(track['song'])

    print(names)
    return names, paths

"""if __name__ == "__main__":
    n, m = get_similar_tracks(get_best_tracks("1944615217")[-5:])
    print(n)
    print(m)"""