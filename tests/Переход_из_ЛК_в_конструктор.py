import time
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

login = driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p") #Клик по кнопке Личный кабинет
login.click()

user_email = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
user_email.send_keys("revaz.mustoyan@yandex.ru")
user_password = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
user_password.send_keys("1234567")
login_finish = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button")#Клик по кнопке Войти
login_finish.click()
time.sleep(1)
element = driver.find_element(By.LINK_TEXT, "Личный Кабинет")#Клик по кнопке Личный кабинет
element.click()
time.sleep(1)
element = driver.find_element(By.LINK_TEXT, "Конструктор")#Клик по кнопке Конструктор
element.click()

time.sleep(1)
construktor_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/h1")#Проверяем что на странице есть слово Соберите бургер
value_construktor_text = construktor_text.text
assert value_construktor_text == 'Соберите бургер'


time.sleep(3)
driver.quit()