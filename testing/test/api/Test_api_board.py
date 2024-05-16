from api.BoardApi import BoardApi


def test_create_board(api_client: BoardApi, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_org_id("664303eecd0e0f41a0ec0727")
    resp = api_client.create_board("New board to be deleted")
    #возьмем из ответа resp значение по полю id и положим его в словарик, который в фикстуре delete board, передаст id для удаления доски
    delete_board["board_id"] = resp.get("id")
    board_list_after = api_client.get_all_boards_by_org_id("664303eecd0e0f41a0ec0727")
    assert len(board_list_after) - len(board_list_before) == 1

def test_delete_board(api_client: BoardApi, dummy_board_id):
    board_list_before = api_client.get_all_boards_by_org_id("664303eecd0e0f41a0ec0727")
    api_client.delete_board_by_id(dummy_board_id)
    board_list_after = api_client.get_all_boards_by_org_id("664303eecd0e0f41a0ec0727")
    assert len(board_list_before) - len(board_list_after) == 1
