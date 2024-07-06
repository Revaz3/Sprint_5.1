from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.constants import Constants
import time
from tests.locators import Locators

class Test_perehod_v_lk:
    def test_perehod_v_lk(seld, driver):
        driver.find_element(*Locators.LICHNII_KABINET).click()  # Клик по кнопке Личный кабинет
        driver.find_element(*Locators.POLE_EMAIL).send_keys(Constants.EMAIL)  # Поле email
        driver.find_element(*Locators.POLE_PASSWORD).send_keys(Constants.PASSWORD)  # Поле password
        driver.find_element(*Locators.KNOPKA_VOITI).click()  # Кнопка войти после ввода емейла и пароля  # Клик по кнопке Войти
        time.sleep(1)
        driver.find_element(*Locators.LICHNII_KABINET).click()  # Клик по кнопке Личный кабинет

        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE)).text
        assert button == 'Профиль'
