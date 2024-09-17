from modules.parameters import Parameters
from modules.window_first import WindowFirst
from modules.window_second import WindowSecond
from modules.window_third import WindowThird


class WindowManager:
    def __init__(self, root):
        self.root = root
        self.P = Parameters()
        self.current_window = None
        # self.switch_to_window_first()

    def switch_to_window_first(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = WindowFirst(root=self.root, manager=self)

    def switch_to_window_second(self, language, native):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = WindowSecond(
            root=self.root, manager=self, language=language, native=native)

    def switch_to_window_third(self, language, native):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = WindowThird(
            root=self.root, manager=self, language=language, native=native)
