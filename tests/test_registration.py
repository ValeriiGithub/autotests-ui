import pytest
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage

@pytest.mark.parametrize(
        'email, username, password',
        [('ivanov@gmail.com', 'ivan', 'qwerty12345')]
)
@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
def test_successful_registration(dashboard_page: DashboardPage, registration_page: RegistrationPage, email, username, password):  # Создаем тестовую функцию
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email, username, password)
    registration_page.click_registration_button()

    dashboard_page.check_visible_dashboard_title()

