import allure
from page.AuthPage import AuthPage
from page.MainPage import MainPage
import pytest

def test_create_board(browser, test_data:dict):
    email = test_data.get("email")
    password = test_data.get("password")
    board_name = test_data.get("board_name")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_create_board()
    main_page.choose_option_to_create()
    main_page.fill_name(board_name)
    main_page.click_save_button()

    info_name = main_page.get_board_name()
    current_url = main_page.get_current_url()

    with allure.step("Проверить, что url " + current_url + "начинается на https://trello.com/b"):
        assert current_url.startswith("https://trello.com/b")
   
    with allure.step("Проверить, что указано название созданной доски"):
        with allure.step("Название доски должно быть " +board_name):
            assert info_name == board_name

def test_delete_board(browser, test_data:dict):
    email = test_data.get("email")
    password = test_data.get("password")
    board_name = test_data.get("board_name")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_create_board()
    main_page.choose_option_to_create()
    main_page.fill_name(board_name)
    main_page.click_save_button()

    main_page.open_side_menu()
    main_page.scroll_menu()
    main_page.click_to_close_board()
    