from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    empty_cart_message = "Ваша корзина пуста"

    def cart_should_be_empty(self):
        assert self.is_not_elements_present(CartPageLocators.CART_ITEMS), "Cart is not empty"

    def text_should_indicate_that_cart_empty(self):
        message = self.browser.find_element(*CartPageLocators.CART_CONTENT).text
        assert self.empty_cart_message in message, \
            "Messages does not match. Expected - %s\n Actual - %s" % (self.empty_cart_message, message)
