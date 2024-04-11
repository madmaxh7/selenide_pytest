from pageobjects.base_web import BaseWebPage, BaseWebElement


class LogoImg(BaseWebElement):

    def __init__(self):
        self.loc = '//img[@alt="Wikipedia"]'


class LoginButton(BaseWebElement):

    def __init__(self):
        self.loc = '//li[@id="pt-login-2"]//span[text()="Log in"]'


class UserNameLink(BaseWebElement):

    def __init__(self):
        self.loc = '//div[@class="vector-header-container"]//a[@class="new"]'


class SearchField(BaseWebElement):

    def __init__(self):
        self.loc = '//div[@id="p-search"]//input[@name="search"]'


class SearchResultDescription(BaseWebElement):

    def __init__(self, loc):
        self.loc = f'{loc}//span[contains(@class, "description")]'


class SearchResult(BaseWebElement):

    def __init__(self, title):
        self.loc = f'//form[@id="searchform"]//ul[@class="cdx-menu__listbox"]/li[@title="{title}"]'

    def description(self):
        return SearchResultDescription(self.loc)


class HomePageEn(BaseWebPage):

    login_button = LoginButton()
    logo_image = LogoImg()
    user_link = UserNameLink()
    search_field = SearchField()

    def click_login(self):
        self.login_button.click()

    @staticmethod
    def search_result(title):
        return SearchResult(title)
