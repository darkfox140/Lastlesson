from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_ADDRESS = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER = (By.CSS_SELECTOR, '#register_form .btn')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages :nth-child(1) div')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    MESSAGE_PRICE = (By.CSS_SELECTOR, '#messages p:nth-child(1)')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '#content_inner p.price_color')
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages p:nth-child(1) strong')


class BasketPageLocators:
    VIEW_BASKET = (By.CSS_SELECTOR, 'span a')
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, '#basket_formset div')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner p a')
