import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class Testlogforma_vosstanovl:
    def test_login_forma_vosstanovl(self, driver):
        email = 'revaz.mustoyan@yandex.ru'
        password = '1234567'
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p[2]/a").click() #Клик по кнопке Восстановить пароль
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p/a").click() #Клик по кнопке Войти

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(email)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(password)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()

        time.sleep(1)
        button_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")
        value_button_text = button_text.text
        assert value_button_text == 'Оформить заказ'