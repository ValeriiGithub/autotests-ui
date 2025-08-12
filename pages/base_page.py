from typing import Pattern
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        '''
        networkidle — если страница делает много динамических запросов, и вы хотите дождаться полной тишины (надежнее, но чуть медленнее).
        '''
        self.page.goto(url, wait_until='networkidle')   # https://stepik.org/lesson/1664944/step/1?discussion=11721105&reply=11723133&unit=1687956

    def reload(self):
        '''
        domcontentloaded — если вы уверены, что нужные вам элементы появляются сразу после загрузки DOM (быстрее, меньше ожиданий).
        '''
        self.page.reload(wait_until='domcontentloaded') # 'domcontentloaded', чтобы дождаться, когда DOM страницы будет полностью загружен.

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)