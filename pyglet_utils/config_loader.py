import configparser


class ConfigLoader(object):
    def __init__(self, debug_file_path):
        self.config = configparser.ConfigParser()
        self.config.read(debug_file_path)

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
