from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import Locators
from tests.constants import Constants
import time


class Test_logout:
    def test_logout(self, driver):
        driver.find_element(*Locators.LICHNII_KABINET).click() #Клик по кнопке Личный кабинет
        driver.find_element(*Locators.POLE_EMAIL).send_keys(Constants.EMAIL)  # Поле email
        driver.find_element(*Locators.POLE_PASSWORD).send_keys(Constants.PASSWORD)  # Поле password
        driver.find_element(*Locators.KNOPKA_VOITI).click()  # Кнопка войти после ввода емейла и пароля
        time.sleep(1)
        driver.find_element(*Locators.LICHNII_KABINET).click() #Клик по кнопке Личный кабинет
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.KNOPKA_LOGOUT)).click() #Клик по кнопке Выйти в личном кабинете
        time.sleep(1)
        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.KNOPKA_VOITI))
        assert button.is_displayed(), "Кнопка 'Войти' не отображается на странице"

