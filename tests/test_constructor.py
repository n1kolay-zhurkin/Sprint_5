from locators.locators import ConstructorLocators

BASE_URL = "https://stellarburgers.education-services.ru"


def test_constructor_tabs(driver):
    driver.get(BASE_URL)

    driver.find_element(*ConstructorLocators.SAUCES_TAB).click()
    driver.find_element(*ConstructorLocators.FILLINGS_TAB).click()
    driver.find_element(*ConstructorLocators.BUNS_TAB).click()

    assert driver.find_element(*ConstructorLocators.BUNS_TAB).is_displayed()

