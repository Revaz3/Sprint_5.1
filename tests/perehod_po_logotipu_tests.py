from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.constants import Constants


class Test_perehod_po_logo:
    def test_perehod_po_logo(seld, driver):
        driver.find_element(By.XPATH, "//a[@href='/account']").click()  # Клик по кнопке Личный кабинет
        driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(Constants.EMAIL)
        driver.find_element(By.XPATH, '//input[@name="Пароль"]').send_keys(Constants.PASSWORD)
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()  # Клик по кнопке Войти
        driver.find_element(By.XPATH, "//a[@href='/account']").click()  # Клик по кнопке Личный кабинет
        driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()  #Клик по логотипу
        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']"))).text
        assert button == 'Соберите бургер'