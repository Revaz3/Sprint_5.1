from selenium.webdriver.common.by import By


class locators():
    voiti_v_akkaunt = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")
    email = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    password = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')