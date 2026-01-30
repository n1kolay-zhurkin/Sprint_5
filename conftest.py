import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    

    driver.maximize_window()
    yield driver
    driver.quit()

# Настройки для тестовых данных
USER_NAME = "TestUser"
USER_EMAIL = "testuser@example.com"
USER_PASSWORD = "12345678"

BASE_URL = "https://stellarburgers.nomoreparties.site/"



