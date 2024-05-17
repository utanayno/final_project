import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from configuration.ConfigProvider import ConfigProvider

class MainPage:

    def __init__(self, driver) -> None:
        self.__driver = driver
    
    @allure.step("Получить текущий url")
    def get_current_url(self) -> str:
        return self.__driver.current_url
    
    @allure.step("Открыть боковое меню")
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-member-menu-button]").click()
    
    @allure.step("Получить информацию о пользователе")
    def get_account_info(self) -> list[str]:
        name = self.__driver.find_element(By.CSS_SELECTOR, ".tS3UagTaVXEivA").text
        email = self.__driver.find_element(By.CSS_SELECTOR, ".AS8ZlkEoqFiwD_").text

        return [name, email]
        
        