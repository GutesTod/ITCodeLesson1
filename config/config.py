import os
from configparser import ConfigParser

CONFIG_DIR = os.path.dirname(__file__)

class Config():
    def __init__(self, path):
        self.cfg = ConfigParser()
        self.cfg.read(path) # извлекаются данные из .ini файла
    def ConfigTelegram(self):
        return self.cfg['API']['TOKEN']

cfg = Config(CONFIG_DIR + '\config.ini')