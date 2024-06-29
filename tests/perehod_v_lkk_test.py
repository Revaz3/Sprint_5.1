import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class Test_perehod_v_lk:
    def test_perehod_v_lk(seld, driver):
        email = 'revaz.mustoyan@yandex.ru'
        password = '1234567'
        driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p").click()  # Клик по кнопке Личный кабинет
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(email)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(password)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()#Клик по кнопке Войти
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p").click()  # Клик по кнопке Личный кабинет
        time.sleep(1)

        time.sleep(1)
        profile_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[1]/a")  # Проверяем что на странице есть слово Профиль
        value_profile_text = profile_text.text
        assert value_profile_text == 'Профиль'