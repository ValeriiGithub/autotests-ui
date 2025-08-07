import pytest  # Импортируем библиотеку pytest
from playwright.sync_api import expect, Page

from pages.login_page import LoginPage


# Тестовые данные: (email, password)
email_and_password = [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password"),
]

# Описания для ids
ids = [
    "Проверяем, что пользователь не может войти в систему с невалидными email и password",
    "Проверяем, что пользователь не может войти в систему с невалидным email, и пустым password",
    "Проверяем, что пользователь не может войти в систему с пустым email, и невалидным password",
]

@pytest.mark.parametrize(
    "email, password",
    email_and_password,
    ids=ids
)
@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.authorization  # Добавили маркировку authorization
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):  # Создаем тестовую функцию
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
    
    