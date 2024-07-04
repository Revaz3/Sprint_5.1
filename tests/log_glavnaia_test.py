import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.constants import Constants


class Testlogglavnaia:
    def test_login_glavnaia(self, driver):
        
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]').click()
        driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(Constants.EMAIL)
        driver.find_element(By.XPATH, '//input[@name="Пароль"]').send_keys(Constants.PASSWORD)
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()

        button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'))).text
        assert button == 'Оформить заказ'