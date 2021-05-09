import pyglet

from data import game

debug = True
main_window = game.GameWindow(debug)
pyglet.app.run()
