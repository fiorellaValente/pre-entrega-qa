"""
Configuración de fixtures para pytest
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """
    Fixture que proporciona un webdriver de Chrome.
    Se ejecuta antes de cada test y se cierra después.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()


@pytest.fixture
def base_url():
    """URL base de la aplicación."""
    return "https://www.saucedemo.com/"