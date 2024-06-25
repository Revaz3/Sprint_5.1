import time
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

login = driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p") #Кнопка Личный кабинет в шапке сайта.
login.click()

user_email = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input") #Ввод в поле email
user_email.send_keys("revaz.mustoyan@yandex.ru")
user_password = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") #Ввод в поле пароль
user_password.send_keys("1234567")
login_finish = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button") #Клик по кнопке Войти
login_finish.click()

time.sleep(2)
button_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")
value_button_text = button_text.text
assert value_button_text == 'Оформить заказ'

time.sleep(3)
driver.quit()
