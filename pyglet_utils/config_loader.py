import configparser
import os


class ConfigLoader(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.getcwd(), "game_config.cfg"))

    def get_window_width(self):
        return int(self.config["window"]["window_width"])

    def get_window_height(self):
        return int(self.config["window"]["window_height"])

    def get_fps_cap(self):
        return float(self.config["window"]["fps_cap"])

    def get_splash_screen_duration_in_seconds(self):
        return int(self.config["splash"]["splash_screen_duration_in_seconds"])

    def get_resources_path(self):
        return self.config["resources"]["resources_path"]

    def get_game_logo(self):
        return self.config["resources"]["game_logo"]
