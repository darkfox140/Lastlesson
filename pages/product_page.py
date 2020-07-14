from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            'Message add to basket is not presented'
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        assert product_name == product_in_basket, 'Name is not same'

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), 'Message price is not presented'
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == product_price_in_basket, 'Price is not sam'