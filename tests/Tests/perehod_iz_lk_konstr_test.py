from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.constants import Constants
from tests.locators import Locators



class Testperehod_lk_konstr:
    def test_perehod_iz_lk_v_konstruktor(self, driver):
        driver.find_element(*Locators.LICHNII_KABINET).click() #Клик по кнопке Личный кабинет
        driver.find_element(*Locators.POLE_EMAIL).send_keys(Constants.EMAIL)  # Поле email
        driver.find_element(*Locators.POLE_PASSWORD).send_keys(Constants.PASSWORD)  # Поле password
        driver.find_element(*Locators.KNOPKA_VOITI).click()  # Кнопка войти после ввода емейла и пароля
        driver.find_element(*Locators.LICHNII_KABINET).click()  # Клик по кнопке Личный кабинет
        driver.find_element(*Locators.KNOPKA_KONSTRUKTOR).click()  # Клик по кнопке конструктор
        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.KNOPKA_SOBERITE_BURGER)).text
        assert button == 'Соберите бургер'


