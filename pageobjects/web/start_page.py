from pageobjects.base_web import BaseWebPage, BaseWebElement
from pageobjects.web.home_page_en import HomePageEn


class LanguageSelect(BaseWebElement):

    def __init__(self, lang):
        super().__init__()
        self.loc = f"//strong[text()='{lang}']/.."


class StartPage(BaseWebPage):
    lang = 'English'

    def select_language(self, language=None):
        language = language or self.lang
        english_lang = LanguageSelect(language)
        english_lang.wait_for_present()
        english_lang.click()
        try:
            from pageobjects.web.sc.bookings.bookings_page import SCBookingsPage
        except ImportError:
            pass
        HomePageEn().logo_image.wait_for_present()
