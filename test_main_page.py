from .pages.main_page import MainPage
from selenium.webdriver.common.by import By


# def should_be_login_link(self):
#     assert self.is_element_present(By.ID, "login_link"), "Login link is not presented"


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
