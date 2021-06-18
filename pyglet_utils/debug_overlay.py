from pyglet_utils import debuggable, utils


class DebugOverlay:
    debuggable_contents = []
    debug_lines = []
    batch = None
    # TODO: get this Y value from the config once that's merged
    y_pos = 450

    def __init__(self, batch):
        self.batch = batch
        self.insert_debug_line(
            debuggable.Debuggable("Debug Menu: (press 0 to toggle)", False)
        )

    def update_debug(self):
        for idx, line in enumerate(self.debuggable_contents):
            if idx >= len(self.debug_lines):
                self.debug_lines.append(
                    utils.create_debug_label(
                        line.get_debug_output(), y_start=self.y_pos, batch=self.batch
                    )
                )
                self.y_pos -= 14
            else:
                self.debug_lines[idx].text = line.get_debug_output()
        return self.debug_lines

    def insert_debug_line(self, value):
        if not isinstance(value, debuggable.Debuggable):
            raise TypeError(
                "Objects added to the debug overlay must be of type Debuggable"
            )
        else:
            self.debuggable_contents.append(value)
