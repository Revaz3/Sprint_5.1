import time
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

button_souse = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]")#Клик по кнопке Соусы
button_souse.click()

time.sleep(1)
souse_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[2]/a[1]/p")#Проверяем что на странице есть продукты из вкладки Начинки
value_souse_text = souse_text.text
assert value_souse_text == 'Соус Spicy-X'

time.sleep(2)
driver.quit()
