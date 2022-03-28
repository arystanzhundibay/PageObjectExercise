import pytest
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators, LoginPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
import time


# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_add_to_bucket_button()
#     page.should_not_be_success_message()
#
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_add_to_bucket_button()
#     page.success_message_disappeared()


# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()


# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()


# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_basket_button()
#     page.basket_is_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, '@#FNaNDF#123fasd')
        button = login_page.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
        login_page.should_be_authorized_user()
        page.browser.implicitly_wait(10)

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        button = browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        #page.solve_quiz_and_get_code()
        messages = browser.find_elements(By.CSS_SELECTOR, 'div.alert strong')
        correct = ['Coders at Work', 'Deferred benefit offer', '£19.99']
        for i in range(len(messages)):
            assert messages[i].text == correct[i], link
