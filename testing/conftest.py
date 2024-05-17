import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):

        timeout = ConfigProvider().getint("ui", "timeout")
        browser_name = ConfigProvider().get("ui", "browser_name")
        
        if browser_name == 'chrome':
            browser = webdriver.Chrome(service=Service((ChromeDriverManager().install())))
        else:
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        
        browser.implicitly_wait(timeout)
        browser.maximize_window()

    yield browser
    
    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def api_client() -> BoardApi:
    url = ConfigProvider().get("api", "base_url")
    return BoardApi(url, "ATTAf9b0498f5aada9e476e2e6ad0945882bff041730e27f9e2e3a9876280b40676fB84E3A13", "8b8770fc6d22a693fc3b92ecda2cc898")

#фикстура для неавторизованного пользователя
@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi(ConfigProvider().get("api", "base_url"), "")

#фикстура для создания доски, которая будет удалена
@pytest.fixture
def dummy_board_id() -> BoardApi:
    api = BoardApi(ConfigProvider().get("api", "base_url"), "ATTAf9b0498f5aada9e476e2e6ad0945882bff041730e27f9e2e3a9876280b40676fB84E3A13", "8b8770fc6d22a693fc3b92ecda2cc898")
    resp = api.create_board("Board to be deleted").get("id")
    return resp

#фикстура для удаления созданной доски
@pytest.fixture
def delete_board():
    dictionary = {"board_id": ""}
    yield dictionary

    api = BoardApi(ConfigProvider().get("api", "base_url"), "ATTAf9b0498f5aada9e476e2e6ad0945882bff041730e27f9e2e3a9876280b40676fB84E3A13", "8b8770fc6d22a693fc3b92ecda2cc898")
    api.delete_board_by_id(dictionary.get("board_id"))
   