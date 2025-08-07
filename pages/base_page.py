from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until='networkidle')   # https://stepik.org/lesson/1664944/step/1?discussion=11721105&reply=11723133&unit=1687956

    def reload(self):
        self.page.reload(wait_until='domcontentloaded') # 'domcontentloaded', чтобы дождаться, когда DOM страницы будет полностью загружен.

'''
domcontentloaded — если вы уверены, что нужные вам элементы появляются сразу после загрузки DOM (быстрее, меньше ожиданий).
networkidle — если страница делает много динамических запросов, и вы хотите дождаться полной тишины (надежнее, но чуть медленнее).
'''