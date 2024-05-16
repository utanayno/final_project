import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from api.BoardApi import BoardApi

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome(service=Service((ChromeDriverManager().install())))
        browser.implicitly_wait(4)
        browser.maximize_window()

    yield browser
    
    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def api_client() -> BoardApi:
    return BoardApi("https://api.trello.com/1", "ATTAf9b0498f5aada9e476e2e6ad0945882bff041730e27f9e2e3a9876280b40676fB84E3A13", "8b8770fc6d22a693fc3b92ecda2cc898")

#фикстура для неавторизованного пользователя
@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi("https://api.trello.com/1", "")

#фикстура для создания доски, которая будет удалена
@pytest.fixture
def dummy_board_id() -> BoardApi:
    api = BoardApi("https://api.trello.com/1", "ATTAf9b0498f5aada9e476e2e6ad0945882bff041730e27f9e2e3a9876280b40676fB84E3A13", "8b8770fc6d22a693fc3b92ecda2cc898")
    resp = api.create_board("Board to be deleted").get("id")
    return resp

#фикстура для удаления созданной доски
@pytest.fixture
def delete_board():
    dictionary = {"board_id": ""}
    yield dictionary

    api = BoardApi("https://api.trello.com/1", "ATTAf9b0498f5aada9e476e2e6ad0945882bff041730e27f9e2e3a9876280b40676fB84E3A13", "8b8770fc6d22a693fc3b92ecda2cc898")
    api.delete_board_by_id(dictionary.get("board_id"))
   