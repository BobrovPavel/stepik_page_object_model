import time

from pages.product_page import ProductPage


# def test_guest_can_add_product_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
#     product_page = ProductPage(browser, 10, link)
#     product_page.open()
#     product_page.add_product_to_card()
#     # time.sleep(5555)
#     assert product_page.should_be_match_the_price() and product_page.should_be_match_the_name(), "Product name or price do not match"


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_not_success_alert_present()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
