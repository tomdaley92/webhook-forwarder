from ruamel import yaml
import os

class Config:
    __DEFAULT_PATH = os.path.expanduser("~") + "/config.yaml"

    def __init__(self, path=__DEFAULT_PATH):
        self.__path = os.path.normpath(path)

    def get(self, *keys):
        with open(self.__path, "r") as file:
            value = yaml.load(file, Loader=yaml.RoundTripLoader)

        for key in keys:
            if isinstance(value, list):
                value = value[key]
            else:
                value = value.get(key, None)
        return value
