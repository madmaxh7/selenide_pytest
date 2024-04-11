from pageobjects.base_web import BaseWebPage, BaseWebElement


class PersonalTitle(BaseWebElement):

    def __init__(self):
        self.loc = f'//main//span[@class="mw-page-title-main"]'


class PersonalPage(BaseWebPage):

    persona_title = PersonalTitle()
