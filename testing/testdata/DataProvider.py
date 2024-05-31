import json
#открой файл и прочитай его содержимое
my_file = open("final_project/testing/test_data.json")
global_data = json.load(my_file)

class DataProvider:
    def __init__(self)-> None:
        self.data = global_data
        
    #метод получает из файла значение настройки
    def get(self, prop) -> str:
        return self.data.get(prop)
    
    #метод получает из файла числовое значение настройки
    #def get(self, prop:str) -> int:
        #val = self.data.get(prop)
        #return int(val)

    #метод получает из файла token
    def get_token(self) -> str:
        return self.data.get("token")
    
    #метод получает из файла token
    def get_key(self) -> str:
        return self.data.get("key")
    
   