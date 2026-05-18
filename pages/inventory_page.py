"""
Página de Inventario - Page Object Model
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class InventoryPage:
    """Representa la página de inventario después del login."""
    
    INVENTORY_CONTAINER = (By.CLASS_NAME, "inventory_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    LOGOUT_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    
    def __init__(self, driver):
        """Inicializa con el webdriver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def is_inventory_displayed(self) -> bool:
        """Verifica si se cargó la página de inventario."""
        try:
            self.wait.until(EC.presence_of_element_located(self.INVENTORY_CONTAINER))
            return True
        except:
            return False
    
    def get_inventory_items_count(self) -> int:
        """Obtiene la cantidad de productos en el inventario."""
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(items)
    
    def logout(self) -> None:
        """Realiza logout."""
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
        self.wait.until(EC.presence_of_element_located(self.LOGOUT_LINK))
        self.driver.find_element(*self.LOGOUT_LINK).click()