import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_constructor_tabs(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    
    tabs = ["Булки", "Соусы", "Начинки"]
    for tab in tabs:
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(),'{tab}')]"))
        ).click()
