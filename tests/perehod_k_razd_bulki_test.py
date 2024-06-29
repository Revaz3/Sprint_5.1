import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class Test_perehod_bulki:
    def test_perehod_bulki(self, driver):
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]").click()  # Клик по кнопке Соусы
        time.sleep(1)
        button_bulki = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]")  # Клик по кнопке Булки
        button_bulki.click()
        time.sleep(1)
        souse_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[1]")  # Проверяем что на странице есть продукты из вкладки Булки
        value_souse_text = souse_text.text
        assert value_souse_text == 'Булки'