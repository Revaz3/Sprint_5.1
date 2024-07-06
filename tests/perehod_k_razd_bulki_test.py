from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import Locators

class Test_perehod_bulki:
    def test_perehod_bulki(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.VKLADKA_SOUSE)).click()  #Клик по кнопке Соусы
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.VKLADKA_BULKI)).click()  # Клик по кнопке Булки

        active_tab_class = driver.find_element(*Locators.AKTIVNAIA_VKLADKA_BULKI).get_attribute('class')
        assert "tab_tab_type_current__2BEPc" in active_tab_class
