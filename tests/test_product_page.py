import time

from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, 10, link)
    product_page.open()
    product_page.add_product_to_card()
    # time.sleep(5555)
    assert product_page.should_be_match_the_price() and product_page.should_be_match_the_name(), "Product name or price do not match"
