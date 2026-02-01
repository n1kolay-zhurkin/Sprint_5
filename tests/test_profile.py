from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.data import USER_EMAIL, USER_PASSWORD
from locators.locators import (
    MainPageLocators,
    LoginPageLocators,
    ProfilePageLocators
)


class TestProfile:

    def test_logout_from_profile(self, driver):
        driver.get("https://stellarburgers.education-services.ru")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(USER_EMAIL)

        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Переход в личный кабинет
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        # Ждём кнопку выхода в профиле
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        assert WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

