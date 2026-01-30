import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        driver_instance = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        driver_instance = webdriver.Firefox(options=options)
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполняем обязательные поля
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    ).send_keys("Николай")

    driver.find_element(By.NAME, "email").send_keys("zhurkin_kolya_qa_36_37@yandex.ru")
    driver.find_element(By.NAME, "password").send_keys("123456789")

    # Нажимаем кнопку регистрации
    driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()

    # Проверяем успешную регистрацию
    success_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Вход')] | //button[contains(text(),'Выйти')]")
        )
    )
    assert success_element.is_displayed(), "Регистрация не прошла!"


def test_registration_with_short_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполняем имя и email
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    ).send_keys("Николай")

    driver.find_element(By.NAME, "email").send_keys("zhurkin_kolya_qa_36_37@yandex.ru")
    driver.find_element(By.NAME, "password").send_keys("123")  # короткий пароль

    driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()

    # Проверяем появление ошибки для короткого пароля
    error_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".input__error"))
    )
    assert "Пароль слишком короткий" in error_element.text, "Сообщение об ошибке не отображается!"


