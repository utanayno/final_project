import requests

class BoardApi:
    base_url = "https://api.trello.com/1"

    def get_all_boards_by_org_id(self, org_id: str) -> dict:
        body = {
            'key': '8b8770fc6d22a693fc3b92ecda2cc898',
            'token': 'ATTAf9b0498f5aada9e476e2e6ad0945882bff041730e27f9e2e3a9876280b40676fB84E3A13'
        }
        path = "{trello}/organizations/{id}/boards".format(trello = self.base_url, id = org_id)
        cookie = {"token": "ATTAf9b0498f5aada9e476e2e6ad0945882bff041730e27f9e2e3a9876280b40676fB84E3A13"}
        resp = requests.get(path, json=body, cookies=cookie)

        return resp.json()

    def create_board(self, name):
        body = {
            'name': name,
            'key': '8b8770fc6d22a693fc3b92ecda2cc898',
            'token': 'ATTAf9b0498f5aada9e476e2e6ad0945882bff041730e27f9e2e3a9876280b40676fB84E3A13'
        }
        #cookie = {"token": "ATTAf9b0498f5aada9e476e2e6ad0945882bff041730e27f9e2e3a9876280b40676fB84E3A13"}
        path = "{trello}/boards/".format(trello = self.base_url)
        resp = requests.post(path, json=body)

        return resp.json()
        