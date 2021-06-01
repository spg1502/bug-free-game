import pyglet_utils.utils
from pyglet_utils.debuggable import Debuggable


class DebugOverlay:
    debug_contents = []
    batch = None

    def __init__(self, batch):
        self.batch = batch
        self.insert_debug_line(Debuggable("Debug Overlay", "(press 0 to toggle)"))

    def update_debug(self):
        debug_lines = []
        for line in self.debug_contents:
            debug_lines.append(line.get_debug_output())

        return pyglet_utils.utils.create_debug_overlay(debug_lines, batch=self.batch)

    def insert_debug_line(self, value):
        if not isinstance(value, Debuggable):
            raise TypeError("Objects added to the debug overlay must be of type Debuggable")
        else:
            self.debug_contents.append(value)
