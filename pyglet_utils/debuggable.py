class Debuggable:

    def __init__(self, class_name, *args):
        self.class_name = class_name

        if isinstance(args[0], str):
            self.debug_text = args[0]

    # All child classes must implement their own get_debug_output
    # By having this raise NotImplementedError, child classes that haven't overwritten this will
    # pass compilation, but will throw an error at runtime only
    def get_debug_output(self):
        if self.debug_text is not None and self.class_name is not None:
            return self.class_name + ": " + self.debug_text
        else:
            raise NotImplementedError
