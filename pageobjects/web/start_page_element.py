from pageobjects.base_web import BaseWebPage, BaseWebElement
from pageobjects.web.base_page_en_element import HomePageEn


class LanguageSelect(BaseWebElement):

    def __init__(self, lang):
        super().__init__()
        self.loc = f"//strong[text()='{lang}']/.."


class LanguageSelectPage(BaseWebElement):
    def __init__(self):
        super().__init__()
        self.en_lang = 'English'

    @property
    def select_en_language(self):
        return LanguageSelect(self.en_lang)


class StartPage(BaseWebPage):

    language_select = LanguageSelectPage()

    def select_en_language_sp(self):
        self.language_select.select_en_language.wait_for_visible()
        self.language_select.select_en_language.click()
        try:
            from pageobjects.web.sc.bookings.bookings_page import SCBookingsPage
        except ImportError:
            pass
        HomePageEn().logo_image.wait_for_present()
