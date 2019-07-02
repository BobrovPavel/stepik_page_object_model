import pytest
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_open_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        mainpage = MainPage(browser, link)
        loginpage = LoginPage(browser, link)
        mainpage.open()
        mainpage.go_to_login_page()
        loginpage.should_be_login_page()

    @pytest.mark.review
    def test_guest_cant_see_product_in_cart_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        cart_page = CartPage(browser, link)
        cart_page.open()
        cart_page.go_to_cart()
        cart_page.cart_should_be_empty()
        cart_page.text_should_indicate_that_cart_empty()



