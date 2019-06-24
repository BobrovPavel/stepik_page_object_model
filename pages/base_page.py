class BasePage(object):
    def __init__(self, browser, timeout, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
