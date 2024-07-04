from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





faker = Faker()

class TestReg_failed:
    def test_reg(self, driver):
        name = 'John'
        email = faker.email()
        password = '1234'
        driver.find_element(By.XPATH, '//a[@href="/account"]').click()  # Клик по кнопке Войти в аккаунт
        driver.find_element(By.XPATH, "//a[@href='/register']").click()
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(name)
        driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(email)
        driver.find_element(By.XPATH, '//input[@name="Пароль"]').send_keys(password)
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        button_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='input__error text_type_main-default']"))).text
        assert button_text == "Некорректный пароль"
