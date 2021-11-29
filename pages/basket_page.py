from base_page import BasePage
from locators import BasketPageLocators


class BasketPage(BasePage):
    def quest_open_basket_on_home_page(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), 'Товар в корзине !'
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), 'В корзине есть товар !'
