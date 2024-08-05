import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Installed drivers and print their paths from conftest in this folder and im using setup method from there

class TestDem:
    def test_Homehr(self,setup):
        driver=setup
        # setup=driver
        print(setup)

        try:
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
            ).send_keys("Admin")
            driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
            driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

            dashboard_displayed = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='Dashboard']"))
            ).is_displayed()
            time.sleep(5)
            assert dashboard_displayed, "Dashboard should be displayed after login"
            print("Login through Chrome was successful")

        except Exception as e:
            print(f"An error occurred: {e}")
            assert False, "Test failed due to an exception"

        finally:
            driver.quit()

if __name__ == "__main__":
    pytest.main()

# pytest -s -v amazon/test_fixture.py --browser chrome this commened we need to run this commend
#     to genrate report we need to run this command
 # pytest -s -v --html=amazon\report.html amazon/test_fixture.py --browser chrome
