import pyglet
import os

game_path = os.path.dirname(os.path.abspath(__file__))
resources_path = os.path.join(game_path, "../resources/")


def logo(x_start, y_start, batch=None):
    return pyglet.sprite.Sprite(
        pyglet.image.load(resources_path + 'game_logo_200x200.png'),
        x=x_start,
        y=y_start,
        batch=batch)
