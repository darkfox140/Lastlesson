from base_page import BasePage
from locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            'Нет сообщения о добавление в корзинну !'
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        assert product_name == product_in_basket, 'Название товара не совпадают !'

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), 'Нет сообщения о стоимости !'
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == product_price_in_basket, 'Цена товара не совпадает !'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            'Сообщение об успехе представлено, но не должно быть !'

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            'Сообщение об успехе исчезло, но не должно быть !'
