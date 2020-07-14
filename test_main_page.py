from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', ['the-shellcoders-handbook_209/?promo=newYear',
                                  'coders-at-work_207/?promo=newYear2019'])
def test_guest_can_add_product_to_basket(browser, link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/{link}'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    page.should_product_in_basket()
    page.should_be_product_price()


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    page.should_product_in_basket()
    page.should_be_product_price()
