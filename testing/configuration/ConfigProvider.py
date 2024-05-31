import configparser

#создать конфиг.парсер
global_config = configparser.ConfigParser()
#вычитать содержимое файла
global_config.read("final_project/testing/test_config.ini")

class ConfigProvider:
    def __init__(self)-> None:
        self.config = global_config
        
    #метод получает из файла значение настройки
    def get(self, section:str, property: str):
        return self.config[section].get(property)
    
    #метод получает из файла числовое значение настройки
    def getint(self, section:str, property: str):
        return self.config[section].getint(property)
    
    #метод получает из файла значение конкретной настройки: из секции ui значение base_url(файл test config)
    def get_ui_url(self):
        return self.config["ui"].get("base_url")