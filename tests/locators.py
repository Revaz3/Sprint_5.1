from selenium.webdriver.common.by import By


class locators():
    voiti_v_akkaunt = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    email = (By.XPATH, '//input[@name="name"]')
    password = (By.XPATH, '//input[@name="Пароль"]')
    lichnii_kabinet = (By.XPATH, '//a[@href="/account"]')
    button_oformit_zakaz = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    email = 'revaz.mustoyan@yandex.ru'
    password = '1234567'