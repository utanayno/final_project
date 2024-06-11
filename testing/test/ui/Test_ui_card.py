import allure
from page.AuthPage import AuthPage
from page.MainPage import MainPage

def test_create_card(browser, test_data:dict):
    email = test_data.get("email")
    password = test_data.get("password")
    board_name = test_data.get("board_name")
    list_name = test_data.get("list_name")
    card_name = test_data.get("card_name")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_create_board()
    main_page.choose_option_to_create()
    main_page.fill_name(board_name)
    main_page.click_save_button()

    main_page.fill_name_list(list_name)
    main_page.confirm_create_list()

    main_page.create_card()
    main_page.fill_name_card(card_name)
    main_page.confirm_create_card()

    info_card_name = main_page.get_card_name()

    with allure.step("Проверить, что указано название созданной карточки"):
        with allure.step("Название доски должно быть " +card_name):
            assert info_card_name == card_name

def test_update_card(browser, test_data:dict):
    email = test_data.get("email")
    password = test_data.get("password")
    board_name = test_data.get("board_name")
    list_name = test_data.get("list_name")
    card_name = test_data.get("card_name")
    updated_card = test_data.get("updated_card_name")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_create_board()
    main_page.choose_option_to_create()
    main_page.fill_name(board_name)
    main_page.click_save_button()

    main_page.fill_name_list(list_name)
    main_page.confirm_create_list()

    main_page.create_card()
    main_page.fill_name_card(card_name)
    main_page.confirm_create_card()
    main_page.open_card()
    main_page.update_card(updated_card)
    info_updated_card = main_page.get_card_name()

    with allure.step("Проверить, что название карточки отредактировано"):
        with allure.step("Название доски должно быть " +updated_card):
            assert info_updated_card == updated_card

              
def test_delete_card(browser, test_data:dict):
    email = test_data.get("email")
    password = test_data.get("password")
    board_name = test_data.get("board_name")
    list_name = test_data.get("list_name")
    card_name = test_data.get("card_name")
    
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_create_board()
    main_page.choose_option_to_create()
    main_page.fill_name(board_name)
    main_page.click_save_button()

    main_page.fill_name_list(list_name)
    main_page.confirm_create_list()

    main_page.create_card()
    main_page.fill_name_card(card_name)
    main_page.confirm_create_card()
    main_page.open_card()
    main_page.click_to_archive()
    main_page.click_to_delete()

    info_card = main_page.check_exists()
        
    with allure.step("Проверить, что карточки нет"):
        assert info_card == False

def test_move_card(browser, test_data:dict):
    email = test_data.get("email")
    password = test_data.get("password")
    board_name = test_data.get("board_name")
    list_name = test_data.get("list_name")
    second_list_name = test_data.get("second_list_name")
    card_name = test_data.get("card_name")
    
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_create_board()
    main_page.choose_option_to_create()
    main_page.fill_name(board_name)
    main_page.click_save_button()

    main_page.fill_name_list(list_name)
    main_page.confirm_create_list()

    main_page.create_card()
    main_page.fill_name_card(card_name)
    main_page.confirm_create_card()
    main_page.create_another_list()
    main_page.fill_name_another_list(second_list_name)
    main_page.confirm_create_another_list()
    main_page.move_card()
    main_page.open_card()

    info_list = main_page.get_list_name()

    with allure.step("Проверить, что у карточки указан второй список"):
        assert info_list == second_list_name


    