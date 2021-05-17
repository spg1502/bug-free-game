import pyglet
import os
from pyglet_utils import config_loader

config_loader = config_loader.ConfigLoader()


def logo(x_start, y_start, batch=None):
    logo_path = os.path.join(
        os.getcwd(), config_loader.get_resources_path(), config_loader.get_game_logo()
    )
    return pyglet.sprite.Sprite(
        pyglet.image.load(logo_path),
        x=x_start,
        y=y_start,
        batch=batch,
    )
