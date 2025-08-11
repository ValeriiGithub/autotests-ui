from playwright.sync_api import expect, Locator
from pages.base_page import BasePage

from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        
        self.login_link: Locator = page.get_by_test_id('registration-page-login-link')
        self.registration_button: Locator = page.get_by_test_id('registration-page-registration-button')
        

    def click_registration_button(self):
        self.registration_button.click()


