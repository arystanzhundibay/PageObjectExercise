from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input[name=\'login-username\']')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[name=\'login-password\']')
    REGISTER_EMAIL = (By.CSS_SELECTOR, 'input[name=\'registration-email\']')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, 'input[name=\'registration-password1\']')
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input[name=\'registration-password2\']')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[value=\'Register\']')


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group")
    BASKET_IS_EMPTY_MESSAGE = (By.ID, 'content_inner')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-safe')
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group")
    BASKET_IS_EMPTY_MESSAGE = (By.ID, 'content_inner')
