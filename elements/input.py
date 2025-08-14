import allure
from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement
from tools.logger import get_logger  # Импортируем get_logger

logger = get_logger("INPUT")  # Инициализируем logger


class Input(BaseElement):
    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "input"

    def get_locator(self,  nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str,  nth: int = 0, **kwargs):
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

    def check_have_value(self, value: str,  nth: int = 0,  **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)


# https://stepik.org/lesson/1664950/step/7?discussion=11774936&reply=11775375&unit=1687960
class InputRaw(Input):
    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "input raw"

    def get_locator(self,  nth: int = 0,  **kwargs) -> Locator:
        locator = self.locator.format(nth, **kwargs)
        if locator.startswith(("//", ".//", "/")) or "[" in locator:
            return self.page.locator(locator).nth(nth)  # XPath
        elif locator.startswith(("#", ".", "[")):
            return self.page.locator(locator).nth(nth)  # CSS
        else:
            return self.page.get_by_test_id(locator).nth(nth)  # test-id