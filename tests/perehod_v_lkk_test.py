from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.constants import Constants
import time

class Test_perehod_v_lk:
    def test_perehod_v_lk(seld, driver):
        driver.find_element(By.XPATH, "//a[@href='/account']").click()  # Клик по кнопке Личный кабинет
        driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(Constants.EMAIL)
        driver.find_element(By.XPATH, '//input[@name="Пароль"]').send_keys(Constants.PASSWORD)
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()  # Клик по кнопке Войти
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@href='/account']").click()  # Клик по кнопке Личный кабинет

        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href= '/account/profile']"))).text
        assert button == 'Профиль'
