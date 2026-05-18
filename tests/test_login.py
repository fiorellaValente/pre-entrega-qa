"""
Tests de Login - Automatización QA
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:
    """Suite de tests para la funcionalidad de Login."""
    
    @pytest.fixture
    def login_page(self, driver, base_url):
        """Fixture que prepara la página de login."""
        page = LoginPage(driver)
        page.navigate(base_url)
        return page
    
    def test_login_exitoso(self, login_page):
        """
        Test: Verificar que el login es exitoso con credenciales válidas.
        
        Precondiciones:
        - Usuario está en la página de login
        
        Pasos:
        1. Ingresar usuario "standard_user"
        2. Ingresar contraseña "secret_sauce"
        3. Hacer clic en Login
        
        Resultado esperado:
        - Se redirige a la página de inventario
        - Se muestran los productos disponibles
        """
        login_page.login("standard_user", "secret_sauce")
        
        inventory = InventoryPage(login_page.driver)
        assert inventory.is_inventory_displayed(), "No se cargó la página de inventario"
        assert inventory.get_inventory_items_count() > 0, "No hay productos disponibles"
    
    def test_login_usuario_invalido(self, login_page):
        """
        Test: Verificar que el login falla con usuario inválido.
        
        Precondiciones:
        - Usuario está en la página de login
        
        Pasos:
        1. Ingresar usuario "usuario_invalido"
        2. Ingresar contraseña "secret_sauce"
        3. Hacer clic en Login
        
        Resultado esperado:
        - Aparece mensaje de error
        - Se mantiene en la página de login
        """
        login_page.login("usuario_invalido", "secret_sauce")
        
        assert login_page.is_error_displayed(), "No apareció mensaje de error"
        assert login_page.is_username_input_visible(), "Se navegó a otra página"
    
    def test_login_contrasena_invalida(self, login_page):
        """
        Test: Verificar que el login falla con contraseña inválida.
        
        Precondiciones:
        - Usuario está en la página de login
        
        Pasos:
        1. Ingresar usuario "standard_user"
        2. Ingresar contraseña "contrasena_incorrecta"
        3. Hacer clic en Login
        
        Resultado esperado:
        - Aparece mensaje de error
        - Se mantiene en la página de login
        """
        login_page.login("standard_user", "contrasena_incorrecta")
        
        assert login_page.is_error_displayed(), "No apareció mensaje de error"
        error_msg = login_page.get_error_message()
        assert "password" in error_msg.lower() or "username" in error_msg.lower()
    
    def test_login_campos_vacios(self, login_page):
        """
        Test: Verificar validación con campos vacíos.
        
        Precondiciones:
        - Usuario está en la página de login
        
        Pasos:
        1. No ingresar usuario ni contraseña
        2. Hacer clic en Login
        
        Resultado esperado:
        - Aparece mensaje de error
        - Se mantiene en la página de login
        """
        login_page.click_login_button()
        
        assert login_page.is_error_displayed(), "No validó campos vacíos"
    
    def test_locked_user(self, login_page):
        """
        Test: Verificar mensaje cuando el usuario está bloqueado.
        
        Precondiciones:
        - Usuario está en la página de login
        
        Pasos:
        1. Ingresar usuario "locked_out_user"
        2. Ingresar contraseña "secret_sauce"
        3. Hacer clic en Login
        
        Resultado esperado:
        - Aparece mensaje indicando que el usuario está bloqueado
        """
        login_page.login("locked_out_user", "secret_sauce")
        
        assert login_page.is_error_displayed(), "No apareció mensaje de error"
        error_msg = login_page.get_error_message()
        assert "locked" in error_msg.lower(), "El mensaje no menciona bloqueo"