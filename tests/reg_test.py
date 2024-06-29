from faker import Faker
import time
from selenium.webdriver.common.by import By


faker = Faker()

class TestReg:
    def test_reg(self, driver):
        name = 'John'
        email = faker.email()
        password = '1234567'
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button").click()  # Клик по кнопке Войти в аккаунт
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a").click()  # Клик по кнопке зарегистрироваться
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(name)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys(password)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        time.sleep(2)
        button_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/h2")
        value_button_text = button_text.text
        assert value_button_text == 'Вход'