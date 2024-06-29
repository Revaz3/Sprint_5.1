import time
from selenium.webdriver.common.by import By
from selenium import webdriver

def test_logout():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    login = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button") #Клик по кнопке Войти в аккаунт
    login.click()

    user_email = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
    user_email.send_keys("revaz.mustoyan@yandex.ru")
    user_password = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
    user_password.send_keys("1234567")
    login_finish = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button")
    login_finish.click()
    time.sleep(1)
    button_lk = driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p")#Клик по кнопке Личный кабинет
    button_lk.click()
    time.sleep(1)
    logout = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button")#Клик по кнопке Выйти в личном кабинете
    logout.click()

    time.sleep(1)
    button_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/h2")
    value_button_text = button_text.text
    assert value_button_text == 'Вход'

    time.sleep(2)
    driver.quit()