from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    ).send_keys("Test User")
    
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("strongpassword")
    driver.find_element(By.XPATH, "//button[contains(., 'Зарегистрироваться')]").click()
    
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Войти в аккаунт')]"))
    )

def test_registration_with_short_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    ).send_keys("Test User")
    
    driver.find_element(By.NAME, "email").send_keys("testuser2@example.com")
    driver.find_element(By.NAME, "password").send_keys("123")
    driver.find_element(By.XPATH, "//button[contains(., 'Зарегистрироваться')]").click()
    
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Некорректный пароль')]"))
    )

