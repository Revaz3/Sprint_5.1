import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")#Вход на страницу с формой регистрации

driver.find_element(By.NAME, "name").send_keys('John')#Заполнение поля email
driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys('123321@mail.ru')
driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input").send_keys('1234')

login_finish = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button")#Клик по кнопке зарегистрироваться
login_finish.click()

time.sleep(2)
warring_text = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(3) > div > p")
value_warring_text = warring_text.text
assert value_warring_text == "Некорректный пароль"
print("Good test")

driver.quit()
