from typing import Pattern

import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        '''
        networkidle — если страница делает много динамических запросов, и вы хотите дождаться полной тишины (надежнее, но чуть медленнее).
        '''
        with allure.step(f'Opening the url "{url}"'):
            self.page.goto(url, wait_until='networkidle')   # https://stepik.org/lesson/1664944/step/1?discussion=11721105&reply=11723133&unit=1687956

    def reload(self):
        '''
        domcontentloaded — если вы уверены, что нужные вам элементы появляются сразу после загрузки DOM (быстрее, меньше ожиданий).
        '''
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until='domcontentloaded') # 'domcontentloaded', чтобы дождаться, когда DOM страницы будет полностью загружен.

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)
            