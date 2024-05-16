import requests

class BoardApi:

    def __init__(self, base_url: str, token: str, key: str) -> None:
        self.base_url = base_url
        self.token = token
        self.key = key
         

    def get_all_boards_by_org_id(self, org_id: str) -> dict:
        
        path = "{trello}/organizations/{id}/boards?key={keyApi}&token={tokenApi}".format(trello = self.base_url, id = org_id, keyApi = self.key, tokenApi = self.token)
        resp = requests.get(path)

        return resp.json()

    def create_board(self, name) -> dict:
        body = {
            'name': name,
            'key': self.key,
            'token': self.token
        }
        
        path = "{trello}/boards/".format(trello = self.base_url)
        resp = requests.post(path, json=body)

        return resp.json()
    
    def delete_board_by_id(self, id: str):
                
        path = path = "{trello}/boards/{board_id}?key={keyApi}&token={tokenApi}".format(trello = self.base_url, board_id = id, keyApi = self.key, tokenApi = self.token)
        resp = requests.delete(path)

        return resp.json()
        