class Debuggable:
    def __init__(self, debug_text=None, show_class_name=True):
        self.show_class_name = show_class_name
        if debug_text is not None:
            self.debug_text = str(debug_text)

    @property
    def class_name(self):
        return self.__class__

    # All child classes must implement their own get_debug_output
    # By having this raise NotImplementedError, child classes that haven't overwritten this will
    # pass compilation, but will throw an error at runtime only
    def get_debug_output(self):
        if self.debug_text is not None:
            if self.show_class_name:
                return str(self.class_name) + ": " + self.debug_text
            else:
                return self.debug_text
        else:
            raise NotImplementedError(
                f"{self.class_name} has not implemented get_debug_output"
            )
