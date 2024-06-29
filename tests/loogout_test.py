import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class Test_logout:
    def test_logout(self, driver):
        email = 'revaz.mustoyan@yandex.ru'
        password = '1234567'
        driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p").click() #Клик по кнопке Личный кабинет
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(email)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(password)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p").click() #Клик по кнопке Личный кабинет
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button").click() #Клик по кнопке Выйти в личном кабинете

        time.sleep(1)
        button_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/h2")
        value_button_text = button_text.text
        assert value_button_text == 'Вход'