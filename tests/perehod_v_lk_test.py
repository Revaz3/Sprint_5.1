import time
from selenium.webdriver.common.by import By
from selenium import webdriver

def test_perehod_v_lk():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    login = driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p")#Клик по кнопке Личный кабинет
    login.click()

    user_email = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input") #Заполняем поле email
    user_email.send_keys("revaz.mustoyan@yandex.ru")
    user_password = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") #Заполняет поле password
    user_password.send_keys("1234567")
    login_finish = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button") #Клик по кнопке Войти
    login_finish.click()
    time.sleep(2)
    element = driver.find_element(By.LINK_TEXT, "Личный Кабинет") #Клик по кнопке Личный кабинет
    element.click()

    time.sleep(1)
    profile_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[1]/a")#Проверяем что на странице есть слово Профиль
    value_profile_text = profile_text.text
    assert value_profile_text == 'Профиль'


    time.sleep(3)
    driver.quit()
