import configparser
import os


class ConfigReader:

    def __init__(self):
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "config.ini"
        )

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get(self, key):
        return self.config["DEFAULT"][key]