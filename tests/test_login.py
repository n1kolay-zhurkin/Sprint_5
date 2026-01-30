from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_with_real_user(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    
    # Входим в аккаунт
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Войти в аккаунт')]"))
    ).click()
    
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    ).send_keys("testuser@example.com")
    
    driver.find_element(By.NAME, "password").send_keys("testpassword")
    driver.find_element(By.XPATH, "//button[contains(., 'Войти')]").click()
    
    # Проверяем, что личный кабинет открылся
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Личный Кабинет')]"))
    )
