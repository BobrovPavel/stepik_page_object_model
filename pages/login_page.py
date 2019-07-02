from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.get_page_url()

    def should_be_login_form(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), "Login form is not displayed"

    def should_be_register_form(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), "Registration form is not displayed"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTRATION_EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTRATION_PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.SUBMIT_REGISTRATION_BUTTON)).click()
