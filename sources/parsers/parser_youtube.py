import os
import yt_dlp


# Функция для поиска
def find_song(query):
    # Настройки yt-dlp для поиска
    ydl_opts = {
        'quiet': True,
        'format': 'bestaudio/best',
        'noplaylist': True,
    }

    # Поиск треков на YouTube
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch10:{query}", download=False)

    # Вывод найденных вариантов
    result = "Найденные варианты:\n" + "\n".join(
        [f"{i}. {entry['title']} - {entry['uploader']}" for i, entry in enumerate(search_results['entries'], 1)]
    )
    result = result + "\n\nВведите номер трека для скачивания или повторите поиск"
    count = len(search_results['entries'])
    return result, search_results['entries'], count

# скачивания песни
def download_song(choice: int, result, save_folder: str):
    selected_track = result[choice - 1]

    # Создаём папку для загрузки, если её нет
    os.makedirs(save_folder, exist_ok=True)

    # Путь для сохранения
    filename = f"{save_folder}/{selected_track['title']}"

    # Настройки yt-dlp для скачивания
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

    # Скачивание выбранного трека
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([selected_track['webpage_url']])

    return filename
