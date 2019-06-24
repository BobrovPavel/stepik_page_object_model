from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, 10, link)
    page.open()
    page.should_be_login_link()


def test_open_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    mainpage = MainPage(browser, 10, link)
    loginpage = LoginPage(browser, 10, link)
    mainpage.open()
    mainpage.go_to_login_page()
    loginpage.should_be_login_page()
