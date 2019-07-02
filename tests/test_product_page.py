import time
import pytest
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage


class TestLoginFromProductPage(object):

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.is_not_success_alert_present()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_card()
        product_page.should_be_match_the_price() and product_page.should_be_match_the_name()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_cart_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        cart_page = CartPage(browser, link)
        cart_page.open()
        cart_page.go_to_cart()
        cart_page.cart_should_be_empty()
        cart_page.text_should_indicate_that_cart_empty()


class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse="True")
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(str(time.time()) + "@gmail.com", "testpassword123")
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.is_not_success_alert_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_card()
        product_page.should_be_match_the_price() and product_page.should_be_match_the_name()
