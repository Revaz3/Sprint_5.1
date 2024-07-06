from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import Locators

class Test_perehod_nachinki:
    def test_perehod_nachinki(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.VKLADKA_NACHINKI)).click()  # Клик по кнопке Начинки

        active_tab_class = driver.find_element(*Locators.AKTIVNAIA_VKLADKA_NACHINKI).get_attribute('class')
        assert "tab_tab_type_current__2BEPc" in active_tab_class
