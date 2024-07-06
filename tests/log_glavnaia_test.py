from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.constants import Constants
from tests.locators import Locators

class Testlogglavnaia:
    def test_login_glavnaia(self, driver):
        driver.find_element(*Locators.VOITI_V_AKKAUNT).click() #Кнопка Войти в аккаунт на главной странице
        driver.find_element(*Locators.POLE_EMAIL).send_keys(Constants.EMAIL)#Поле email
        driver.find_element(*Locators.POLE_PASSWORD).send_keys(Constants.PASSWORD)#Поле password
        driver.find_element(*Locators.KNOPKA_VOITI).click()#Кнопка войти после ввода емейла и пароля

        button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.KNOPKA_OFORMIT_ZAKAZ)) #Кнопка оформить заказ на главной странице
        assert button.is_displayed(), "Кнопка 'Оформить заказ' не отображается на странице"