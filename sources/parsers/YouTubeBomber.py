import os
import yt_dlp

def find_in_youtube(query: str):
    # Настройки yt-dlp для поиска
    ydl_opts = {
        'quiet': True,
        'format': 'bestaudio/best',
        'noplaylist': True,
        'default_search': 'ytsearch10',  # Ищем 10 результатов
    }

    # Поиск треков
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(query, download=False)

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
    if 1 <= choice <= len(result):
        selected_track = result[choice - 1]
        filename = os.path.join(save_folder, f"{selected_track['title']}.mp3")

        # Настройки для скачивания
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

        # Скачивание
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([selected_track['webpage_url']])

        return True, selected_track
    else:
        return False

