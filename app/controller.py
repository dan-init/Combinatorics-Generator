from model import MathOperations, UiFunctions
from ui import Gui

class Controller:
    def __init__(self, math_functions: MathOperations, ui_functions:UiFunctions, view:Gui) -> None:
        self.math_functions = math_functions
        self.ui_functions = ui_functions
        self.view = view

    def test_function(self):
        self.view.result_string.set()

    def run(self) -> None:
        self.view.mainloop()