import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class Testperehod_lk_konstr:
    def test_perehod_iz_lk_v_konstruktor(seld, driver):
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
        driver.find_element(By.LINK_TEXT, "Конструктор").click()  # Клик по кнопке конструктор

        time.sleep(1)
        construktor_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/h1")  # Проверяем что на странице есть слово Соберите бургер
        value_construktor_text = construktor_text.text
        assert value_construktor_text == 'Соберите бургер'