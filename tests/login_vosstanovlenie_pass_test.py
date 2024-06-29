import time
from selenium.webdriver.common.by import By
from selenium import webdriver

def test_login_vosstanovl_pass():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    time.sleep(2)
    login = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button") #Клик по кнопке Войти в аккаунт
    login.click()
    time.sleep(2)
    login_0 = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p[2]/a") #Клик по кнопке Восстановить пароль
    login_0.click()
    time.sleep(2)
    login_1 = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p/a") #Клик по кнопке Войти
    login_1.click()
    time.sleep(2)

    user_email = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
    user_email.send_keys("revaz.mustoyan@yandex.ru")
    user_password = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
    user_password.send_keys("1234567")
    login_finish = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button")
    login_finish.click()

    time.sleep(2)
    button_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")
    value_button_text = button_text.text
    assert value_button_text == 'Оформить заказ'

    time.sleep(3)
    driver.quit()
