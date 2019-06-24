import time

from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_card(self):
        add_to_card_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON)
        add_to_card_button.click()
        self.solve_quiz_and_get_code()

    def should_be_match_the_text(self, string, substring):
        try:
            str = self.browser.find_element(*string).text
            sub = self.browser.find_element(*substring).text
        except NoSuchElementException:
            print("No elements found on page.")
            return False
        return sub in str

    def should_be_match_the_price(self):
        return self.should_be_match_the_text(ProductPageLocators.CARD_PRODUCT_PRICE, ProductPageLocators.PRODUCT_PRICE)

    def should_be_match_the_name(self):
        return self.should_be_match_the_text(ProductPageLocators.PRODUCT_NAME, ProductPageLocators.SUCCESS_ALERT_PRODUCT_NAME)
