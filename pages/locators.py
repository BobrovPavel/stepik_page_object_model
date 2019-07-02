from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    OPEN_CART_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")


class CartPageLocators(object):
    CART_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    CART_CONTENT = (By.CSS_SELECTOR, "#content_inner")


class LoginPageLocators(object):
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    SUBMIT_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators(object):
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main")
    CARD_PRODUCT_PRICE = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
