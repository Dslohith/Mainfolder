# import pytest
#
#
#
# class TestClassM:
#     @pytest.mark.parametrize('num1, num2', [(1, 1), (2, 3), (4, 5)])
#     def test_cal(self, num1, num2):
#         assert num1 == num2

# parametrozation can be done in two ways 1st one is not convinet
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Install drivers and print their paths
chromedriver_path = ChromeDriverManager().install()
print(f"Chromedriver path: {chromedriver_path}")


class TestdemoHrm:
    @pytest.mark.parametrize('username,password',
                             [("Admin", "admin123"),
                              ("admin", "admin1236"),
                              ("Admin", "admin123")])
    def test_Hrm(self, username, password):
        chrome_service = ChromeService(chromedriver_path)
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php")
        time.sleep(5)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))).send_keys(username)

        driver.find_element(By.XPATH, value="//input[@placeholder='Password']").send_keys(password)
        driver.find_element(By.XPATH, value="//button[normalize-space()='Login']").click()
        time.sleep(5)
        try:
            status = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='Dashboard']"))).is_displayed()
            # status=driver.find_element(By.XPATH,value="//h6[normalize-space()='Dashboard']").is_displayed()
            driver.quit()
            assert self.status == True
            print("login throgh the chrome")
        except:
            driver.quit()
            assert False
