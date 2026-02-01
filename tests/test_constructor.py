from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import ConstructorLocators


class TestConstructor:

    def test_switch_to_sauces_tab(self, driver):
        driver.get("https://stellarburgers.education-services.ru")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)
        ).click()

        active_tab = driver.find_element(*ConstructorLocators.ACTIVE_TAB)
        assert active_tab.text == "Соусы"

    def test_switch_to_fillings_tab(self, driver):
        driver.get("https://stellarburgers.education-services.ru")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.FILLINGS_TAB)
        ).click()

        active_tab = driver.find_element(*ConstructorLocators.ACTIVE_TAB)
        assert active_tab.text == "Начинки"

    def test_switch_to_buns_tab(self, driver):
        driver.get("https://stellarburgers.education-services.ru")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.BUNS_TAB)
        ).click()

        active_tab = driver.find_element(*ConstructorLocators.ACTIVE_TAB)
        assert active_tab.text == "Булки"
