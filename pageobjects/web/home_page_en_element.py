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


class HomePageEn(BaseWebPage):

    login_button = LoginButton()
    logo_image = LogoImg()
    user_link = UserNameLink()

    def click_login(self):
        self.login_button.click()
