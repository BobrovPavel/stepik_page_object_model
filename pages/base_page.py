import math
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, 15)

    def open(self):
        self.browser.get(self.url)

    def go_to_cart(self):
        cart_button = self.browser.find_element(*MainPageLocators.OPEN_CART_BUTTON)
        cart_button.click()

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def get_page_url(self):
        return self.browser.current_url

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        alert = self.browser.switch_to.alert
        print("Your code: {}".format(alert.text))
        alert.accept()

    def should_be_authorized_user(self):
        assert self.is_element_present(MainPageLocators.USER_ICON), "User icon is not presented," \
                                                                    " probably unauthorised user"

    def is_not_elements_present(self, locator, timeout=4):
        # Мы уже находимся на странице, на которой нужно выполнить проверку
        try:
            # Мы ищем пока появится элемент (точно также, как и во все остальных случаях)
            # Но так как элемента на странцие быть не должно - мы получаем ошибку
            WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:  # Здесь мы пытаемся "поймать" эту ошибку.
            return True  # И если элемента нет и возникает ошибка - возвращаем True

        return False  # Если ошибки нет - нам вернется False (полная противоположность методу "is_element_present"

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True
