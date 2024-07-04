import time

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

faker = Faker()

class TestReg:
    def test_reg(self, driver):
        name = 'John'
        email = faker.email()
        password = '1234567'

        driver.find_element(By.XPATH, '//a[@href="/account"]').click()  # Клик по кнопке Войти в аккаунт
        driver.find_element(By.XPATH, "//a[@href='/register']").click()
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(name)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(email)
        driver.find_element(By.XPATH, '//input[@name="Пароль"]').send_keys(password)
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        time.sleep(1)
        button = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"))).text
        assert button == 'Войти'