import inspect
import importlib
from . import __submodule__

def printFunctionCode(func_name):
    for submodule in __submodule__:
        try:
            module = importlib.import_module(f"zar.{submodule}")
            func = getattr(module, func_name, None)
            if func and callable(func):
                print(inspect.getsource(func))
                return
        except ModuleNotFoundError:
            pass

    print(f"Function '{func_name}' not found in vezor package.")

class Printer:
    def __getattr__(self, name):
        return lambda: printFunctionCode(name)

algoPrint = Printer()
