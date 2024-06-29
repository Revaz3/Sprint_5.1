import time
from selenium.webdriver.common.by import By
from selenium import webdriver

def test_perehod_po_logotipu():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    login = driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p") #Клик по кнопке Личный кабинет
    login.click()

    user_email = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
    user_email.send_keys("revaz.mustoyan@yandex.ru")
    user_password = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
    user_password.send_keys("1234567")
    login_finish = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button") #Клик по кнопке Войти
    login_finish.click()
    time.sleep(1)
    login = driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p") #Клик по кнопке Личный кабинет
    login.click()
    time.sleep(1)
    element_logo = driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2") #Клик по логотипу
    element_logo.click()

    time.sleep(1)
    logo_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/h1")#Проверяем переход на главную страницу
    value_logo_text = logo_text.text
    assert value_logo_text == 'Соберите бургер'


    time.sleep(2)
    driver.quit()