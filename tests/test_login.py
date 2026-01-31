from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.data import USER_EMAIL, USER_PASSWORD
from locators.locators import (
    MainPageLocators,
    LoginPageLocators,
    RegistrationPageLocators
)


def test_login_via_main_page(driver):
    driver.get("https://stellarburgers.education-services.ru")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            MainPageLocators.LOGIN_BUTTON
        )
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            LoginPageLocators.EMAIL_INPUT
        )
    ).send_keys(USER_EMAIL)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            LoginPageLocators.PASSWORD_INPUT
        )
    ).send_keys(USER_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            LoginPageLocators.LOGIN_BUTTON
        )
    ).click()

    # Проверка успешного входа
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            MainPageLocators.PERSONAL_ACCOUNT_BUTTON
        )
    )


def test_login_via_personal_account_button(driver):
    driver.get("https://stellarburgers.education-services.ru")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            MainPageLocators.PERSONAL_ACCOUNT_BUTTON
        )
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            LoginPageLocators.EMAIL_INPUT
        )
    ).send_keys(USER_EMAIL)

    driver.find_element(
        *LoginPageLocators.PASSWORD_INPUT
    ).send_keys(USER_PASSWORD)

    driver.find_element(
        *LoginPageLocators.LOGIN_BUTTON
    ).click()

    # Проверка успешного входа
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            MainPageLocators.PERSONAL_ACCOUNT_BUTTON
        )
    )


def test_login_via_registration_form(driver):
    driver.get("https://stellarburgers.education-services.ru/register")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            RegistrationPageLocators.LOGIN_LINK
        )
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            LoginPageLocators.EMAIL_INPUT
        )
    ).send_keys(USER_EMAIL)

    driver.find_element(
        *LoginPageLocators.PASSWORD_INPUT
    ).send_keys(USER_PASSWORD)

    driver.find_element(
        *LoginPageLocators.LOGIN_BUTTON
    ).click()

    # Проверка успешного входа
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            MainPageLocators.PERSONAL_ACCOUNT_BUTTON
        )
    )