import pyglet
from enum import Enum


class GameStates(Enum):
    SPLASH_SCREEN = 0
    MAIN_MENU = 1
    PLAYING = 2
