from typing import Pattern

import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', 'Title')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'Button')

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        '''
        Важно! 
        https://stepik.org/lesson/1664955/step/7?unit=1687965#:~:text=%D0%92%D0%B0%D0%B6%D0%BD%D0%BE!%20%D0%94%D0%BB%D1%8F,%D1%87%D0%B5%D1%82%D0%BA%D0%BE%20%D0%B8%20%D0%BA%D0%BE%D1%80%D1%80%D0%B5%D0%BA%D1%82%D0%BD%D0%BE.
        '''
        self.button.click()
        self.check_current_url(expected_url)
