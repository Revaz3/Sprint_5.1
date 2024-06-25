import time
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

button_nachinki = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]")#Клик по кнопке Начинки
button_nachinki.click()

time.sleep(1)
nachinki_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[3]/a[1]/p")#Проверяем что на странице есть продукты из вкладки Начинки
value_nachinki_text = nachinki_text.text
assert value_nachinki_text == 'Мясо бессмертных моллюсков Protostomia'

time.sleep(2)
driver.quit()
