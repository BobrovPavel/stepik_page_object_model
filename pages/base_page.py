from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    def __init__(self, browser, timeout, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def get_page_url(self):
        return self.browser.current_url
