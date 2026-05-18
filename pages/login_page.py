"""
Página de Login - Page Object Model
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LoginPage:
    """Representa la página de login de SauceDemo."""
    
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")
    
    def __init__(self, driver):
        """Inicializa con el webdriver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def navigate(self, url="https://www.saucedemo.com/"):
        """Navega a la página de login."""
        self.driver.get(url)
    
    def enter_username(self, username: str) -> None:
        """Ingresa el usuario."""
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
    
    def enter_password(self, password: str) -> None:
        """Ingresa la contraseña."""
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
    
    def click_login_button(self) -> None:
        """Hace clic en el botón Login."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def login(self, username: str, password: str) -> None:
        """Realiza login con usuario y contraseña."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self) -> str:
        """Obtiene el mensaje de error si existe."""
        try:
            error = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
            return error.text
        except TimeoutException:
            return ""
    
    def is_error_displayed(self) -> bool:
        """Verifica si hay mensaje de error."""
        try:
            self.driver.find_element(*self.ERROR_MESSAGE)
            return True
        except NoSuchElementException:
            return False
    
    def is_username_input_visible(self) -> bool:
        """Verifica si el campo username está visible."""
        try:
            self.driver.find_element(*self.USERNAME_INPUT)
            return True
        except NoSuchElementException:
            return False