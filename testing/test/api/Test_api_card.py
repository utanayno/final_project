from api.BoardApi import BoardApi
from api.CardApi import CardApi
import allure

def test_create_card(api_client_2: CardApi, dummy_board_id, test_data:dict, delete_board: dict):
    list_name = test_data.get("list_name")
    card_name = test_data.get("card_name")
    id_list = api_client_2.create_list(list_name, dummy_board_id).get("id")
    id_card = api_client_2.create_card(card_name, id_list).get("id")
    created_card_id = api_client_2.get_card_by_id(id_card).get("id")
    delete_board["board_id"] = dummy_board_id
    
    with allure.step("Проверить, что создана карточка по id " +id_card):
        assert  created_card_id == id_card

def test_update_card(api_client_2: CardApi, dummy_board_id, test_data:dict, delete_board: dict):
    list_name = test_data.get("list_name")
    card_name = test_data.get("card_name")
    updated_card_name = test_data.get("updated_card_name")
    id_list = api_client_2.create_list(list_name, dummy_board_id).get("id")
    id_card = api_client_2.create_card(card_name, id_list).get("id")
    new_card_name = api_client_2.update_card(id_card, updated_card_name).get("name")
    
    updated_card = api_client_2.get_card_by_id(id_card).get("name")
    delete_board["board_id"] = dummy_board_id
    
    with allure.step("Проверить, что у карточки изменено название на " +new_card_name):
        assert  new_card_name == updated_card

def test_delete_card(api_client_2: CardApi, dummy_board_id, test_data:dict, delete_board: dict):
    list_name = test_data.get("list_name")
    card_name = test_data.get("card_name")
    id_list = api_client_2.create_list(list_name, dummy_board_id).get("id")
    id_card = api_client_2.create_card(card_name, id_list).get("id")
    card_list_before = api_client_2.get_list_of_cards(dummy_board_id)
    api_client_2.delete_card_by_id(id_card)
    card_list_after = api_client_2.get_list_of_cards(dummy_board_id)
    
    delete_board["board_id"] = dummy_board_id
    with allure.step("Проверить, что количество карточек на доске уменьшилось на 1"):
        assert len(card_list_before) - len(card_list_after) == 1

def test_move_card_to_another_list(api_client_2: CardApi, dummy_board_id, test_data:dict, delete_board: dict):
    list_name_1 = test_data.get("list_name")
    list_name_2 = test_data.get("second_list_name")
    card_name = test_data.get("card_name")
    id_list_1 = api_client_2.create_list(list_name_1, dummy_board_id).get("id")
    id_list_2 = api_client_2.create_list(list_name_2, dummy_board_id).get("id")
    id_card = api_client_2.create_card(card_name, id_list_1).get("id")
    id_list_after_moving = api_client_2.move_card_to_another_list(id_card, id_list_2).get("idList")
    id_list_of_updated_card = api_client_2.get_card_by_id(id_card).get("idList")
    delete_board["board_id"] = dummy_board_id
    
    with allure.step("Проверить, что карточка перемещена в другой список"):
        assert id_list_after_moving == id_list_of_updated_card

    
   