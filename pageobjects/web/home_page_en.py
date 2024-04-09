from pageobjects.base_web import BaseWebPage, BaseWebElement


class LogoImg(BaseWebElement):

    def __init__(self):
        self.loc = '//img[@alt="Wikipedia"]'


class LoginButton(BaseWebElement):

    def __init__(self):
        self.loc = '//li[@id="pt-login-2"]//span[text()="Log in"]'


class HomePageEn(BaseWebPage):

    login_button = LoginButton()
    logo_image = LogoImg()

    def click_login(self):
        self.login_button.click()
