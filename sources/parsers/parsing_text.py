from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from chromedriver_py import binary_path
from langdetect import detect, LangDetectException


# Функция для инициализации браузера
def init_browser():
    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)
    return driver


# Функция для определения языка текста
def detect_language(text):
    """Определяет язык текста с помощью langdetect"""
    if not text or len(text.strip()) < 10:  # Минимальная длина для надежного определения
        return "unknown"

    try:
        return detect(text)
    except LangDetectException:
        return "unknown"


# Основная функция парсинга
def get_song_lyrics(song_name):
    """Get song lyrics from musify.club with language detection"""
    url = f'https://musify.club/search?searchText={song_name}'
    driver = init_browser()
    lyrics = None
    found_song_name = None
    language = None

    try:
        driver.get(url)
        time.sleep(2)  # Wait for page to load

        # Find the first playlist element
        first_song = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.playlist.playlist--hover .playlist__item:first-child'))
        )

        # Get song name
        found_song_name = first_song.find_element(By.CSS_SELECTOR, "a.strong").text

        # URL to song page
        page_first_song = first_song.find_element(By.CSS_SELECTOR, "a.strong").get_attribute("href")

        driver.get(page_first_song)
        time.sleep(2)  # Wait for page to load

        # Wait for "Lyrics" button to be clickable
        btn_text = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="bodyContent"]/div/div[3]/ul/li[1]/a'))
        )

        # Scroll to element and click via JavaScript
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_text)
        driver.execute_script("arguments[0].click();", btn_text)

        # Wait for lyrics to load
        text_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tabLyrics"]/div/div/div'))
        )
        lyrics = text_element.text

        # Определяем язык текста
        if lyrics:
            language = detect_language(lyrics)

    except Exception as e:
        return None, None, None
    finally:
        driver.quit()

    return found_song_name, lyrics, language


"""if __name__ == "__main__":
    # Проверка работы парсера текстов песен
    test_song = "ддт что такое осень"  # Можно заменить на любую другую песню

    print(f"Пробуем найти текст для песни: {test_song}")
    found_name, lyrics, language = get_song_lyrics(test_song)

    print("\nРезультат:")
    print(f"Название: {found_name}")
    print(f"Язык текста: {language if language else 'не определен'}")
    print(f"Текст:\n{lyrics if lyrics else 'Не удалось найти текст'}")"""