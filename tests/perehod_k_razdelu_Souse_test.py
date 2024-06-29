import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class Test_perehod_souse:
    def test_perehod_souse(self, driver):
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]").click()  # Клик по кнопке Соусы

        time.sleep(1)
        souse_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[2]")  # Проверяем что на странице есть продукты из вкладки Начинки
        value_souse_text = souse_text.text
        assert value_souse_text == 'Соусы'