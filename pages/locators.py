from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form .btn')
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(1)')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(1) div strong')
    MESSAGE_PRICE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info.fade.in div p:nth-child(1)')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.col-sm-6.product_main p.price_color')
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, '.in div p:nth-child(1) strong')



