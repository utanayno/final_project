import requests
import allure

class CardApi:

    def __init__(self, base_url: str, token: str, key: str) -> None:
        self.base_url = base_url
        self.token = token
        self.key = key

    @allure.step("Создать список")     
    def create_list(self, name: str, idBoard: str) -> dict:
        body = {
            'name': name,
            'idBoard' : idBoard,
            'key': self.key,
            'token': self.token
            
        }
        
        path = "{trello}/lists".format(trello = self.base_url)
        resp = requests.post(path, json=body)

        return resp.json()
    
    @allure.step("Создать карточку")
    def create_card(self, name: str, idList: str) -> dict:
        body = {
            'name': name,
            'idList' : idList,
            'key': self.key,
            'token': self.token
            
        }
        
        path = "{trello}/cards".format(trello = self.base_url)
        resp = requests.post(path, json=body)

        return resp.json()
    
    @allure.step("Получить карточку по id")
    def get_card_by_id(self, id: str) -> dict:
        
        path = "{trello}/cards/{id}?key={keyApi}&token={tokenApi}".format(trello = self.base_url, id = id, keyApi = self.key, tokenApi = self.token)
        resp = requests.get(path)

        return resp.json()
    
    @allure.step("Обновить данные по карточке (название)")
    def update_card(self, id: str, new_name: str) -> dict:
        body = {
            'name': new_name,
            'key': self.key,
            'token': self.token
            
        }
        
        path = "{trello}/cards/{id}".format(trello = self.base_url, id = id)
        resp = requests.put(path, json=body)

        return resp.json()
    
    @allure.step("Получить список всех карточек на доске")
    def get_list_of_cards(self, id: str) -> dict:
        
        path = "{trello}/boards/{id}/cards?key={keyApi}&token={tokenApi}".format(trello = self.base_url, id = id, keyApi = self.key, tokenApi = self.token)
        resp = requests.get(path)

        return resp.json()
    
    @allure.step("Удалить карточку по id - {id}")
    def delete_card_by_id(self, id: str):
                
        path = path = "{trello}/cards/{id}?key={keyApi}&token={tokenApi}".format(trello = self.base_url, id = id, keyApi = self.key, tokenApi = self.token)
        resp = requests.delete(path)

        return resp.json()
    
    @allure.step("Переместить карточку в другой список")
    def move_card_to_another_list(self, card_id: str, new_list_id: str) -> dict:
        body = {
            'idList': new_list_id,
            'key': self.key,
            'token': self.token
            
        }
        
        path = "{trello}/cards/{id}".format(trello = self.base_url, id = card_id)
        resp = requests.put(path, json=body)

        return resp.json()
    

    
    