mport time
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
time.sleep(1)
button_souse = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]")#Клик по кнопке Соусы
button_souse.click()
time.sleep(1)
button_bulki = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]")#Клик по кнопке Булки
button_bulki.click()

time.sleep(1)
bulki_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]/p")#Проверяем что на странице есть продукты из вкладки Булки
value_bulki_text = bulki_text.text
assert value_bulki_text == 'Флюоресцентная булка R2-D3'
time.sleep(2)
driver.quit()