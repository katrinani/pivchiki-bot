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

def text_par(name_song: str):
    web_text = f'https://www.beesona.pro/songs/?search={name_song}'
    driver = init_browser()
    try:
        driver.get(web_text)
        time.sleep(2)  # Ожидание загрузки страницы

        first_song = driver.find_element(By.XPATH, '//*[@id="grid-1"]/div/div[1]/div/a').get_attribute('href')


        driver.get(first_song)
        time.sleep(2)

        first_song_name = driver.find_element(By.CLASS_NAME, 'copys').find_element(By.CLASS_NAME, 'm153').text

        file_text = driver.find_element(By.CLASS_NAME, 'm207').text

        return file_text
    except Exception:
        print(f"NULL")
    finally:
        driver.quit()


