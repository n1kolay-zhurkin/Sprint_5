from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout_from_profile(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    
    # Входим
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    ).send_keys("testuser@example.com")
    
    driver.find_element(By.NAME, "password").send_keys("testpassword")
    driver.find_element(By.XPATH, "//button[contains(., 'Войти')]").click()
    
    # Переходим в профиль
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Личный Кабинет')]"))
    ).click()
    
    # Выход
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Выход')]"))
    ).click()
    
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Войти в аккаунт')]"))
    )

