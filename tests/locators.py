from selenium.webdriver.common.by import By


class Locators:
    VOITI_V_AKKAUNT = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]') #Кнопка Войти в аккаунт на главной странице
    POLE_EMAIL = (By.XPATH, '//input[@name="name"]') #Поле email
    POLE_PASSWORD = (By.XPATH, '//input[@name="Пароль"]') #Поле password
    POLE_NAME = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input") #Поле имя
    LICHNII_KABINET = (By.XPATH, '//a[@href="/account"]') #Кнопка личный кабинет на главной странице
    KNOPKA_OFORMIT_ZAKAZ = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]') #Кнопка оформить заказ на главной странице
    KNOPKA_VOITI = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') #Кнопка войти после ввода емейла и пароля
    KNOPKA_VOSSTANOVIT_PAROL = (By.XPATH, '//a[@href ="/forgot-password"]')# Клик по кнопке Восстановить пароль
    KNOPKA_VOITI_VOSSTAN_PASSWORD = (By.XPATH, "//a[@class='Auth_link__1fOlj']") #Кнопка  Войти после нажатия "восстановить пароль"
    KNOPKA_LOGOUT = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")# Клик по кнопке Выйти в личном кабинете
    KNOPKA_KONSTRUKTOR = (By.LINK_TEXT, "Конструктор")#Кнопка конструктор
    KNOPKA_SOBERITE_BURGER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']") #Кнопка соберите бургер на главной странице
    LOGOTIP_SAITA = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")#Логотип
    PROFILE = (By.XPATH, "//a[@href= '/account/profile']")#Профиль
    KNOPKA_REGISTRACIA = (By.XPATH, "//a[@href='/register']") #Кнопка Регистрация
    KNOPKA_ZAREGISTRIROVATCA = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") #Кнопка зарегистрироваться
    NEKORREKTNII_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default']") # Некорректный пароль
    VKLADKA_SOUSE = (By.CSS_SELECTOR, "div > main > section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2) > div:nth-child(2)") #Вкладка соусы
    VKLADKA_BULKI = (By.CSS_SELECTOR, "div > main > section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2) > div:nth-child(1)") #Вкладка булки
    VKLADKA_NACHINKI = (By.CSS_SELECTOR, "div > main > section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2) > div:nth-child(3)") #Вкладка начинки
