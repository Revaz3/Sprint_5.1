import time
from selenium.webdriver.common.by import By
from selenium import webdriver

def test_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")#Вход на страницу с формой регистрации


    user_name = driver.find_element(By.NAME, "name")#Заполение поля Имя
    user_name.send_keys("John")
    time.sleep(1)
    user_email = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")#Заполнение поля email
    user_email.send_keys("vzwwr.mezse@yandex.ru")
    time.sleep(1)
    user_password = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input")#Заполнение поля password
    user_password.send_keys("1234567")
    time.sleep(1)

    login_finish = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button")#Клик по кнопке зарегистрироваться
    login_finish.click()
    time.sleep(2)
    button_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/h2")
    value_button_text = button_text.text
    assert value_button_text == 'Вход'

    time.sleep(2)
    driver.quit()