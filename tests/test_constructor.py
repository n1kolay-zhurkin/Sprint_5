from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import ConstructorLocators

BASE_URL = "https://stellarburgers.education-services.ru"


def test_constructor_tabs(driver):
    driver.get(BASE_URL)

    # Соусы
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            ConstructorLocators.SAUCES_TAB
        )
    ).click()

    # Начинки
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            ConstructorLocators.FILLINGS_TAB
        )
    ).click()

    # Булки
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            ConstructorLocators.BUNS_TAB
        )
    ).click()

    assert driver.find_element(
        *ConstructorLocators.BUNS_TAB
    ).is_displayed()
