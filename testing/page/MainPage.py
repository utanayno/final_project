import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from configuration.ConfigProvider import ConfigProvider
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException  
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

    @allure.step("Создать список")
    def create_list(self):
        self.__driver.find_element(By.CSS_SELECTOR, "#board > div > button > span").click()

    @allure.step("Указать имя списка = {list_name}")
    def fill_name_list(self, list_name: str):
        self.__driver.find_element(By.CSS_SELECTOR, "textarea[data-testid=list-name-textarea").send_keys(list_name)

    @allure.step("Нажать 'Добавить список'")
    def confirm_create_list(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=list-composer-add-list-button]").click()
        #почему-то с WebDriverWait не работал тест, со sleep работает. Может неправильно написала (пробовала несколько вариантов?)
        #WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bPNGI_VbtbXQ8v")))
        #WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2[data-testid=list-name]")))
        #WebDriverWait(self.__driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h2[data-testid=list-name]"), 'Test list'))
        sleep(3)

    @allure.step("Создать карточку")
    def create_card(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=list-add-card-button]").click()

    @allure.step("Указать имя карточки = {card_name}")
    def fill_name_card(self, card_name: str):
        self.__driver.find_element(By.CSS_SELECTOR, "textarea[data-testid=list-card-composer-textarea]").send_keys(card_name)
    
    @allure.step("Нажать 'Добавить карточку'")
    def confirm_create_card(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=list-card-composer-add-card-button]").click()
         #почему-то с WebDriverWait не работал тест, со sleep работает. Может неправильно написала (пробовала несколько вариантов?)
        #WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".RD2CmKQFZKidd6")))
        #WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid=card-name]")))
        sleep(3)

    @allure.step("Получить название карточки")
    def get_card_name(self) -> str:
        name = self.__driver.find_element(By.CSS_SELECTOR, "a[data-testid=card-name]").text
        return name
        
    
    @allure.step("Открыть карточку")
    def open_card(self):
        self.__driver.find_element(By.CSS_SELECTOR, ".amUfYqLTZOvGsn").click()
        sleep(3)

    @allure.step("Отредактировать название карточки = {updated_card}")
    def update_card(self, updated_card: str ):
        self.__driver.find_element(By.CSS_SELECTOR, "textarea[data-testid=card-back-title-input]").click()
        self.__driver.find_element(By.CSS_SELECTOR, "textarea[data-testid=card-back-title-input]").clear()
        self.__driver.find_element(By.CSS_SELECTOR, "textarea[data-testid=card-back-title-input]").send_keys(updated_card)
        self.__driver.find_element(By.CSS_SELECTOR, "span[data-testid=CloseIcon]").click()
        sleep(3)

    @allure.step("Нажать на 'Архивировать'")
    def click_to_archive(self):
        element_archive = self.__driver.find_element(By.CSS_SELECTOR,"a[data-testid=card-back-archive-button]")
        element_delete = self.__driver.find_element(By.CSS_SELECTOR,"a[data-testid=card-back-delete-card-button]")
        actions = ActionChains(self.__driver)
        actions.move_to_element(element_archive).click(element_archive).perform()
        actions.move_to_element(element_delete).click(element_delete).perform()

    @allure.step("Нажать на 'Удалить'")
    def click_to_delete(self):
        element = self.__driver.find_element(By.CSS_SELECTOR,"input[value='Удалить']")
        actions = ActionChains(self.__driver)
        actions.move_to_element(element).click(element).perform()

    @allure.step("Проверить отсутствие карточки")
    def check_exists(self):
        try:
            self.__driver.find_element(By.CSS_SELECTOR, "a[data-testid=card-name]")
        except NoSuchElementException:
            return False
        return True
    
    @allure.step("Нажать 'Добавить еще список'")
    def create_another_list(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=list-composer-button]").click()
    
    @allure.step("Указать имя списка = {second_list_name}")
    def fill_name_another_list(self, second_list_name: str):
        self.__driver.find_element(By.CSS_SELECTOR, "textarea.oe8RymzptORQ7h[data-testid=list-name-textarea]").send_keys(second_list_name)

    @allure.step("Нажать 'Добавить список'")
    def confirm_create_another_list(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=list-composer-add-list-button]").click()
        #почему-то с WebDriverWait не работал тест, со sleep работает. Может неправильно написала (пробовала несколько вариантов?)
        #WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bPNGI_VbtbXQ8v")))
        #WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2[data-testid=list-name]")))
        #WebDriverWait(self.__driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h2[data-testid=list-name]"), 'Test list'))
        sleep(3)

    @allure.step("Переместить карточку в другую колонку")
    def move_card(self):
        element = self.__driver.find_element(By.CSS_SELECTOR,"div[data-testid=trello-card]")
        distination = self.__driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ol:nth-child(1) > li:nth-child(2) > div:nth-child(1) > div:nth-child(4) > button:nth-child(1)")
        actions = ActionChains(self.__driver)
        actions.drag_and_drop(element, distination).perform()

    @allure.step("Получить название списка у карточки")
    def get_list_name(self) -> str:
        name = self.__driver.find_element(By.CSS_SELECTOR, "a.js-open-move-from-header").text
        return name

       

    