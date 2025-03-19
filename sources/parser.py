import requests
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
        time.sleep(5)  # Ожидание загрузки страницы

        error_message = driver.find_elements(By.CSS_SELECTOR, 'small.text-red')
        if error_message:
            return "Ошибка: По вашему запросу ничего не найдено."

        first_song = driver.find_element(By.CSS_SELECTOR, '.playlist.playlist--hover .playlist__item:first-child')
        download_link_element = first_song.find_element(By.CSS_SELECTOR, 'a[download]')

        download_link = download_link_element.get_attribute('href')
        file_name = download_link_element.get_attribute('download')

        # Скачивание файла
        response = requests.get(download_link)
        if response.status_code == 200:
            if not os.path.exists('audio'):
                os.makedirs('audio')
            file_path = os.path.join('audio', file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return f'Файл сохранен: {file_path}'
        else:
            return 'Не удалось скачать файл'

    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        driver.quit()

if __name__ == "__main__":
    print(main("Кино Кукушка"))
