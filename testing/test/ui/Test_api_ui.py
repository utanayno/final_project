import allure
from page.AuthPage import AuthPage
from page.MainPage import MainPage
from api.BoardApi import BoardApi
from api.CardApi import CardApi


def test2_create_card(browser, test_data:dict, api_client_2: CardApi, api_client: BoardApi):
    email = test_data.get("email")
    password = test_data.get("password")
    board_name = test_data.get("board_name")
    list_name = test_data.get("list_name")
    card_name = test_data.get("card_name")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    board_id = api_client.create_board(board_name).get("id")
    api_client_2.create_list(board_id, list_name)
    
    main_page = MainPage(browser)
    main_page.create_card()
    main_page.fill_name_card(card_name)
    main_page.confirm_create_card()

    info_card_name = main_page.get_card_name()

    with allure.step("Проверить, что указано название созданной карточки"):
        with allure.step("Название доски должно быть " +card_name):
            assert info_card_name == card_name