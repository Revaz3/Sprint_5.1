import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class Testlogshapka:
    def test_login_shapka(self, driver):
        email = 'revaz.mustoyan@yandex.ru'
        password = '1234567'
        driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p").click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(email)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(password)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()

        time.sleep(1)
        button_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")
        value_button_text = button_text.text
        assert value_button_text == 'Оформить заказ'