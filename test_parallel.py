import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

# Install drivers and print their paths
chromedriver_path = ChromeDriverManager().install()
print(f"Chromedriver path: {chromedriver_path}")

edgedriver_path = EdgeChromiumDriverManager().install()
print(f"Edge driver path: {edgedriver_path}")

geckodriver_path = GeckoDriverManager().install()
print(f"Geckodriver path: {geckodriver_path}")

class TestLogin:
    def test_loginchrome(self):
        chrome_service = ChromeService(chromedriver_path)
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://www.google.co.in/")
        driver.quit()
        print("login throgh the chrome")

    def test_login_edge(self):
        edge_service = EdgeService(edgedriver_path)
        driver = webdriver.Edge(service=edge_service)
        driver.get("https://www.google.co.in/")
        driver.quit()
        print("login throigh edge")

    def test_loginfirefox(self):
        firefox_service = FirefoxService(geckodriver_path)
        driver = webdriver.Firefox(service=firefox_service)
        driver.get("https://www.google.co.in/")
        driver.quit()
        print("logoin throgh firefox")
