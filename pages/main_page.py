from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "en-gb": "Your basket is empty.",
    "en-US": "Your basket is empty.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def click_basket_button(self):
        button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        button.click()

    def basket_is_empty(self):
        language = self.browser.current_url.split('/')[3]
        message = self.browser.find_element(*MainPageLocators.BASKET_IS_EMPTY_MESSAGE).text
        assert languages[language] in message
