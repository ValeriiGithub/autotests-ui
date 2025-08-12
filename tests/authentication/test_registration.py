import pytest
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.parametrize(
        'email, username, password',
        [('ivanov@gmail.com', 'ivan', 'qwerty12345')]
)
@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
class TestRegistration:

    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage, email, username, password):  # Создаем тестовую функцию
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(
            email, 
            username, 
            password
            )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()

