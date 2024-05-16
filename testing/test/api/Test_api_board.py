from api.BoardApi import BoardApi

def test_get_boards():
    api = BoardApi()
    board_list = api.get_all_boards_by_org_id("664303eecd0e0f41a0ec0727")
    
    assert len(board_list.get("boards")) == 0

def test_create_board():
    api = BoardApi()
    board_list_before = api.get_all_boards_by_org_id("664303eecd0e0f41a0ec0727")

    api.create_board("Test board")
    board_list_after = api.get_all_boards_by_org_id("664303eecd0e0f41a0ec0727")
    assert len(board_list_after) - len(board_list_before) == 1
