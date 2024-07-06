import time
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import Locators

faker = Faker()

class TestReg:
    def test_reg(self, driver):
        name = 'John'
        email = faker.email()
        password = '1234567'

        driver.find_element(*Locators.VOITI_V_AKKAUNT).click()  # Клик по кнопке Войти в аккаунт
        driver.find_element(*Locators.KNOPKA_REGISTRACIA).click()  # Клик по кнопке регистрация
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(name)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(email)
        driver.find_element(By.XPATH, '//input[@name="Пароль"]').send_keys(password)
        driver.find_element(*Locators.KNOPKA_ZAREGISTRIROVATCA).click()
        time.sleep(1)
        button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.KNOPKA_VOITI))
        assert button.is_displayed(), "Кнопка 'Войти' не отображается на странице"