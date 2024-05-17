import allure
from page.AuthPage import AuthPage
from page.MainPage import MainPage
import pytest

#@pytest.mark.skip

def test_auth(browser):
    email = "cahifa2331@rencr.com"
    password = "12345678TTT"
    username = "Julia"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()
    with allure.step("Проверить, что url " + current_url + "заканчивается на cahifa2331/boards"):
        assert current_url.endswith("cahifa2331/boards")
   
    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть " +username):
            assert info[0] == username
        with allure.step("Электронная почта должна быть " +email):
            assert info[1] == email
