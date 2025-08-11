from playwright.sync_api import Page, expect, Locator

from components.base_component import BaseComponent


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)


        self.email_input: Locator = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input: Locator = page.get_by_test_id('login-form-password-input').locator('input')


    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def check_visible(self, email: str, password: str):
         self.email_input.fill(email)
         expect(self.email_input).to_have_value(email)

         self.password_input.fill(password)
         expect(self.password_input).to_have_value(password)

