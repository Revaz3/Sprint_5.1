from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import Locators

class Test_perehod_souse:
    def test_perehod_souse(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.VKLADKA_SOUSE)).click()

        active_tab_class = driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']").get_attribute('class')
        assert "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect" in active_tab_class
