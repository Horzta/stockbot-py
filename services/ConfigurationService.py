import configparser

class ConfigurationService:
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def get(self, section, key):
        return self.config[section][key]