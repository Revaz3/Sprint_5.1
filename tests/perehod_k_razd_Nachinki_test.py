import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class Test_perehod_bulki:
    def test_perehod_bulki(self, driver):
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]").click()  # Клик по кнопке Начинки
        time.sleep(1)
        souse_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[3]")  # Проверяем что на странице активна вкладка Начинки
        value_souse_text = souse_text.text
        assert value_souse_text == 'Начинки'