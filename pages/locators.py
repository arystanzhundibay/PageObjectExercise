from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input[name=\'login-username\']')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[name=\'login-password\']')
    REGISTER_EMAIL = (By.CSS_SELECTOR, 'input[name=\'registration-email\']')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, 'input[name=\'registration-password1\']')
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input[name=\'registration-password2\']')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-safe')
