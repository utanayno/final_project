import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from configuration.ConfigProvider import ConfigProvider
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class MainPage:

    def __init__(self, driver) -> None:
        self.__driver = driver
                
    
    @allure.step("Получить текущий url")
    def get_current_url(self) -> str:
        return self.__driver.current_url
    
    @allure.step("Открыть верхнее боковое меню")
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-member-menu-button]").click()
    
    @allure.step("Получить информацию о пользователе")
    def get_account_info(self) -> list[str]:
        name = self.__driver.find_element(By.CSS_SELECTOR, ".tS3UagTaVXEivA").text
        email = self.__driver.find_element(By.CSS_SELECTOR, ".AS8ZlkEoqFiwD_").text
        return [name, email]
    
    @allure.step("Нажать кнопку 'Создать/+' в шапке")
    def open_create_board(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-create-menu-button]").click()

    @allure.step("Выбрать в списке 'Создайте доску'")
    def choose_option_to_create(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-create-board-button]").click()

    @allure.step("Указать имя доски = {board_name}")
    def fill_name(self, board_name: str):
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid=create-board-title-input]").send_keys(board_name)

    @allure.step("Нажать 'Создать'")
    def click_save_button(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=create-board-submit-button]").click()
        WebDriverWait(self.__driver, 10).until(EC.url_contains("https://trello.com/b"))

    @allure.step("Получить название доски")
    def get_board_name(self) -> str:
        name = self.__driver.find_element(By.CSS_SELECTOR, "h1[data-testid=board-name-display]").text
        return name
    
    @allure.step("Открыть боковое меню")
    def open_side_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button.frrHNIWnTojsww.GDunJzzgFqQY_3.bxgKMAm3lq5BpA.HAVwIqCeMHpVKh.SEj5vUdI3VvxDc").click()
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".board-menu-header-title.js-board-menu-title-text")))
            
    @allure.step("Проскроллить меню до пункта 'Закрыть доску'")
    def scroll_menu(self):
        element = self.__driver.find_element(By.CSS_SELECTOR,".board-menu-navigation-item-link.board-menu-navigation-item-link-v2.js-close-board")
        actions = ActionChains(self.__driver)
        actions.move_to_element(element).click(element).perform()
        
    @allure.step("Нажать 'Закрыть доску'")
    def click_to_close_board(self):
        self.__driver.find_element(By.CSS_SELECTOR,"input[data-testid=close-board-confirm-button]").click()
    