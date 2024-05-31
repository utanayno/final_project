import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

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
    DataProvider().get_token()
    DataProvider().get_key()
    url = ConfigProvider().get("api", "base_url")
    return BoardApi(url, DataProvider().get_token(), DataProvider().get_key())

#фикстура для неавторизованного пользователя
@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi(ConfigProvider().get("api", "base_url"), "")

#фикстура для создания доски, которая будет удалена
@pytest.fixture
def dummy_board_id() -> BoardApi:
    DataProvider().get_token()
    DataProvider().get_key()
    api = BoardApi(ConfigProvider().get("api", "base_url"), DataProvider().get_token(), DataProvider().get_key())
    resp = api.create_board("Board to be deleted").get("id")
    return resp 

#фикстура для удаления созданной доски
@pytest.fixture
def delete_board():
    DataProvider().get_token()
    DataProvider().get_key()
    dictionary = {"board_id": ""}
    yield dictionary

    api = BoardApi(ConfigProvider().get("api", "base_url"), DataProvider().get_token(), DataProvider().get_key())
    api.delete_board_by_id(dictionary.get("board_id"))

#фикстура для тестовых данных
@pytest.fixture
def test_data():
    return DataProvider()
   