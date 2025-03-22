from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from chromedriver_py import binary_path

# Функция для инициализации браузера
def init_browser():
    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)
    return driver

# Основная функция парсинга
def main(name_song: str):
    url = f'https://musify.club/search?searchText={name_song}'
    driver = init_browser()

    try:
        driver.get(url)
        time.sleep(2)  # Ожидание загрузки страницы

        # Находим первый элемент плейлиста
        first_song = driver.find_element(By.CSS_SELECTOR, '.playlist.playlist--hover .playlist__item:first-child')

        #Название песни
        first_song_name = first_song.find_element(By.CSS_SELECTOR, "a.strong").text

        #URL на страницу с песней
        page_first_song = first_song.find_element(By.CSS_SELECTOR, "a.strong").get_attribute("href")

        driver.get(f'{page_first_song}')
        time.sleep(2)  # Ожидание загрузки страницы

        #Кнопка открытия текста
        btn_text = driver.find_element(By.XPATH, '//*[@id="bodyContent"]/div/div[3]/ul/li[1]/a')

        #Обработчика клика для открытия текста
        btn_text.click()

        # Находим поле с текстом
        text_element = driver.find_element(By.XPATH, '//*[@id="tabLyrics"]/div/div/div')

        # Получаем текст
        file_text = text_element.text

        print(first_song_name)
        print(file_text)

        if not os.path.exists('text'):
            os.makedirs('text')
        file_path = os.path.join('text', first_song_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(file_text)
        print(f'Файл сохранен: {file_path}')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main("Король и Шут Кукла Колдуна")