import allure
from api.BoardApi import BoardApi

def test_create_board(api_client: BoardApi, delete_board: dict, test_data:dict):
    org_id = test_data.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    resp = api_client.create_board("New board to be deleted")
    #возьмем из ответа resp значение по полю id и положим его в словарик, который в фикстуре delete board, передаст id для удаления доски
    delete_board["board_id"] = resp.get("id")
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    with allure.step("Проверить, что количество досок увеличилось на 1"):
        assert len(board_list_after) - len(board_list_before) == 1

def test_delete_board(api_client: BoardApi, dummy_board_id, test_data:dict):
    org_id = test_data.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    api_client.delete_board_by_id(dummy_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    
    with allure.step("Проверить, что количество досок уменьшилось на 1"):
        assert len(board_list_before) - len(board_list_after) == 1

