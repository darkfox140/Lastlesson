from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK)
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.browser.current_url, 'Ссылка для входа не найдена !'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Нет формы Login !'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Нет формы Register !'

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        password_field2.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER)
        button_submit.click()
