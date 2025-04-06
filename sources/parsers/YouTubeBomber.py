import os
import yt_dlp
from sources.postgres.sql_requests import save_song_to_db
from sources.parsers.parsing_text import get_song_lyrics
from sources.recomendations.text_recomendation import get_text_vector
from sources.recomendations.text_llm_recomendation import get_llm_text_vector
from sources.recomendations.physical_recomendations import extract_svd_features

def find_in_youtube(query: str):
    # Настройки yt-dlp для поиска

    ydl_opts = {
        'quiet': True,
        'format': 'bestaudio/best',
        'noplaylist': True,
        'extract_flat': True,
    }

    # Поиск треков
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch10:{query}", download=False)

    if 'entries' not in search_results or not search_results['entries']:
        return False, "Ничего не найдено, попробуйте другой запрос."

    result = "Найденные варианты:\n" + "\n".join(
        [f"{i}. {entry['title']} - {entry.get('uploader', 'Неизвестный автор')}" for i, entry in enumerate(search_results['entries'], 1)]
    )
    result = result + "\n\nВведите номер трека для скачивания или повторите поиск"
    count = len(search_results['entries'])

    return True, result, search_results['entries'], count


def download_song(result, choice: int, save_folder: str):
    os.makedirs(save_folder, exist_ok=True)
    if isinstance(choice, int) and 1 <= choice <= len(result):
        selected_track = result[choice - 1]
        filename = os.path.join(save_folder, f"{selected_track['title']}.mp3")

        # Download settings
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': filename,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,
        }
        youtube_url = selected_track.get('webpage_url') or selected_track.get(
            'url') or f"https://youtube.com/watch?v={selected_track.get('id', '')}"

        # Download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        mp3_path = f"{filename}"
        print("путь загружен")
        features = extract_svd_features(mp3_path)
        print("фичи загружены")

        title, lyrics, language = get_song_lyrics(selected_track['title'])
        print("текст загружен")
        text_vector = get_text_vector(lyrics).tolist()
        print("текст вектор загружен")
        text_llm_vector = get_llm_text_vector(lyrics)
        print("текст ллм вектор загружен")

        save_song_to_db(
            title=title,
            file_path=mp3_path,
            lyrics = lyrics,
            language = language,
            text_vector = text_vector,
            text_llm_vector = text_llm_vector,
            features = features.tolist()
        )

        return True, selected_track
    else:
        return False

"""
if __name__ == "__main__":
    f1, f2 = extract_svd_features("ДДТ - Что такое осень (Official video).mp3.mp3")
    print(f1)
    print(f2)
    save_song_to_db(
            title="sdfsf",
            file_path="sdfsf",
            lyrics="sdfv sdfv sdfg dfsfdg snfdndfgndgndgngngsfdg",
            language="english",
            text_vector = get_text_vector("sdfsdfsdfsdf").tolist(),
            text_llm_vector = get_llm_text_vector("sdfsdf")
        )"""