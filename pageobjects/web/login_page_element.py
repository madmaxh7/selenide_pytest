from pageobjects.base_web import BaseWebPage, BaseWebElement
from pageobjects.web import constants
from pageobjects.web.base_page_en_element import HomePageEn


class UserNameField(BaseWebElement):

    def __init__(self, loc):
        super().__init__()
        self.loc = f'{loc}//input[@id="wpName1"]'


class PasswordField(BaseWebElement):

    def __init__(self, loc):
        super().__init__()
        self.loc = f'{loc}//input[@id="wpPassword1"]'


class LoginButton(BaseWebElement):

    def __init__(self, loc):
        super().__init__()
        self.loc = f'{loc}//button[@id="wpLoginAttempt"]'


class UserLoginFormPage(BaseWebElement):
    def __init__(self):
        super().__init__()
        self.loc = '//div[@id="userloginForm"]'

    @property
    def username(self):
        return UserNameField(self.loc)

    @property
    def password(self):
        return PasswordField(self.loc)

    @property
    def login_button(self):
        return LoginButton(self.loc)


class LoginPage(BaseWebPage):

    login_form = UserLoginFormPage()

    def fill_login_form(self, username=constants.USERNAME, password=constants.PASSWORD, login=False):
        self.login_form.username.wait_for_present()
        self.login_form.username.send_keys(username)
        self.login_form.password.send_keys(password)
        if login:
            self.login_form.login_button.click()
