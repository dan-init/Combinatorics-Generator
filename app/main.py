from controller import Controller
from model import MathOperations, UiFunctions
from ui import Gui

def main() -> None:
    math_functions = MathOperations()
    ui_functions = UiFunctions()
    view = Gui(math_functions, ui_functions)
    controller = Controller(math_functions, ui_functions, view)
    controller.run()

if __name__ == "__main__":
    main()