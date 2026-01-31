from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.data import USER_NAME
from locators.locators import RegistrationPageLocators, MainPageLocators
from generators import generate_email, generate_password


def test_successful_registration(driver):
    email = generate_email()
    password = generate_password()

    driver.get("https://stellarburgers.education-services.ru/register")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            RegistrationPageLocators.NAME_INPUT
        )
    ).send_keys(USER_NAME)

    driver.find_element(
        *RegistrationPageLocators.EMAIL_INPUT
    ).send_keys(email)

    driver.find_element(
        *RegistrationPageLocators.PASSWORD_INPUT
    ).send_keys(password)

    driver.find_element(
        *RegistrationPageLocators.REGISTER_BUTTON
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            MainPageLocators.PERSONAL_ACCOUNT_BUTTON
        )
    )


def test_registration_with_short_password(driver):
    email = generate_email()
    short_password = "12345"

    driver.get("https://stellarburgers.education-services.ru/register")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            RegistrationPageLocators.NAME_INPUT
        )
    ).send_keys(USER_NAME)

    driver.find_element(
        *RegistrationPageLocators.EMAIL_INPUT
    ).send_keys(email)

    driver.find_element(
        *RegistrationPageLocators.PASSWORD_INPUT
    ).send_keys(short_password)

    driver.find_element(
        *RegistrationPageLocators.REGISTER_BUTTON
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            RegistrationPageLocators.PASSWORD_ERROR
        )
    )

    assert driver.find_element(
        *RegistrationPageLocators.PASSWORD_ERROR
    ).is_displayed()