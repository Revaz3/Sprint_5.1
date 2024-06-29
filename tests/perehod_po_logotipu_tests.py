import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class Test_perehod_po_logo:
    def test_perehod_po_logo(seld, driver):
        email = 'revaz.mustoyan@yandex.ru'
        password = '1234567'
        driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p").click()  # Клик по кнопке Личный кабинет
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(email)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(password)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()#Клик по кнопке Войти
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p").click()  # Клик по кнопке Личный кабинет
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()  #Клик по логотипу
        time.sleep(1)

        time.sleep(1)
        logo_text = driver.find_element(By.XPATH,
                                        "//*[@id='root']/div/main/section[1]/h1")  # Проверяем переход на главную страницу
        value_logo_text = logo_text.text
        assert value_logo_text == 'Соберите бургер'