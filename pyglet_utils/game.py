import random
import string
from time import time

import pyglet
import pyglet.clock
import pyglet.gl as pgl
from pyglet.window import key

from pyglet_utils import utils, load, debug_overlay, debuggable

pgl.glEnable(pgl.GL_BLEND)
pgl.glBlendFunc(pgl.GL_SRC_ALPHA, pgl.GL_ONE_MINUS_SRC_ALPHA)

# TODO: we should move these to a config file
fps_cap = 120.0
window_width = 800
window_height = 450
splash_screen_duration_in_seconds = 1


# TODO: move this to its own separate class file
class GameStates:
    SPLASH_SCREEN = 0
    MAIN_MENU = 1
    PLAYING = 2


class GameWindow(pyglet.window.Window):
    def __init__(self, debug, *args, **kwargs):
        super(GameWindow, self).__init__(window_width, window_height, *args, **kwargs)

        self.game_state = GameStates.SPLASH_SCREEN

        # TODO: Add FPS to debug overlay
        #START: test code for testing debug overlay
        self.test_debug = debuggable.Debuggable("Test_debug", "test")
        #END: test code for testing debug overlay
        self.debug_overlay_batch = pyglet.graphics.Batch()
        self.debug_overlay = debug_overlay.DebugOverlay(self.debug_overlay_batch)
        self.debug_overlay.insert_debug_line(debuggable.Debuggable("Test", "test debug text"))
        self.debug_overlay.update_debug()
        if debug:
            self.debug = True

        # using pyglet batches to improve the efficiency of rendering sprites and text that appear together:
        # https://pyglet.readthedocs.io/en/latest/modules/graphics/#batches-and-groups
        self.splash_screen_batch = pyglet.graphics.Batch()
        self.splash_screen_title, self.splash_screen_logo = self.create_splash_screen(
            self.splash_screen_batch
        )

        self.main_menu_batch = pyglet.graphics.Batch()
        self.main_menu = self.create_main_menu(self.main_menu_batch)

        self.key_handler = key.KeyStateHandler()
        self.push_handlers(self.key_handler)

        # Now that all game elements are loaded, we can start calling update
        pyglet.clock.schedule_interval(self.update, 1.0 / fps_cap)

    def create_splash_screen(self, splash_screen_batch):
        splash_screen_title = utils.create_h1_label(
            "Splash Screen!", 400, window_height - 42, splash_screen_batch
        )
        splash_screen_logo = load.logo(300, 150, splash_screen_batch)
        self.splash_screen_has_been_visible_since = time()

        return splash_screen_title, splash_screen_logo

    def create_main_menu(self, main_menu_batch):
        game_title = utils.create_h1_label(
            "Game Name!", 400, window_height - 42, main_menu_batch
        )
        menu_label_texts = ["Start", "Exit"]
        return (
            utils.create_menu_labels(
                menu_label_texts, 400, window_height - 150, batch = main_menu_batch
            ),
            game_title,
        )

    def on_draw(self):
        self.clear()

        if self.game_state == GameStates.SPLASH_SCREEN:
            self.splash_screen_batch.draw()
        elif self.game_state == GameStates.MAIN_MENU:
            self.main_menu_batch.draw()
        # elif self.game_state == GameStates.PLAYING:
        # self.game_batch.draw()
        # etc...
        if self.debug:
            self.debug_overlay_batch.draw()

    def update(self, dt):
        if self.debug:
            self.debug_overlay.update_debug()
            # print(pyglet.clock.get_fps())

        if self.game_state == GameStates.SPLASH_SCREEN:
            if (
                    time() - splash_screen_duration_in_seconds
                    > self.splash_screen_has_been_visible_since
            ):
                self.game_state = GameStates.MAIN_MENU

    def on_key_press(self, symbol, modifiers):
        # Handles key presses for menus, keyboard shortcuts, and debug menu(s)
        if symbol == key._0 or symbol == key.NUM_0:
            self.debug = not self.debug
            #START: debug overlay stuff
        if symbol == key.BRACKETLEFT:
            self.debug_overlay.insert_debug_line(self.test_debug)
        if symbol == key.BRACKETRIGHT:
            self.test_debug.debug_text = (''.join(random.choice(string.ascii_letters) for i in range(5)))
            #END: debug overlay stuff
