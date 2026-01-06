import pytest
from playwright.sync_api import sync_playwright, Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
        email = "user@gmail.com"
        username = "user"
        password = "password"

        registration_page = RegistrationPage(page=chromium_page)
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.fill_registration_form(email=email, username=username, password=password)
        registration_page.click_registration_button()

        dashboard_page = DashboardPage(page=chromium_page)
        dashboard_page.check_visible_dashboard_title()