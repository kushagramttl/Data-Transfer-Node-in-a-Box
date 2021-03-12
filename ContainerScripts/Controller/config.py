import json


class ConfigSingleton:
    __instance = None
    config_dict = dict()

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ConfigSingleton.__instance == None:
            ConfigSingleton()
        return ConfigSingleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ConfigSingleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ConfigSingleton.__instance = self

    def set_config_values(self):
        with open('config.json') as config_file:
            loaded_dict = json.load(config_file)
            for key, val in loaded_dict.items():
                self.config_dict[key] = val
