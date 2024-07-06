
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import Locators
from tests.constants import Constants


class Testlogshapka:
    def test_login_shapka(self, driver):
        driver.find_element(*Locators.LICHNII_KABINET).click() #кнопка Личный кабинет шапка сайта
        driver.find_element(*Locators.POLE_EMAIL).send_keys(Constants.EMAIL)  # Поле email
        driver.find_element(*Locators.POLE_PASSWORD).send_keys(Constants.PASSWORD)  # Поле password
        driver.find_element(*Locators.KNOPKA_VOITI).click()  # Кнопка войти после ввода емейла и пароля

        button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.KNOPKA_OFORMIT_ZAKAZ)).text #Кнопка оформить заказ на главной странице
        assert button == 'Оформить заказ'