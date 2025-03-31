import inspect
from . import __submodule__

class InputAnalyzer:
    def analyze_function(self, function_name):
        for submodule_name, module in __submodule__.items():
            try:
                func = getattr(module, function_name, None)
                if func and inspect.isfunction(func):
                    signature = inspect.signature(func)
                    params = signature.parameters
                    
                    input_details = {
                        name: str(param) for name, param in params.items()
                    }
                    
                    print(f"Function '{function_name}' requires the following inputs:")
                    for name, detail in input_details.items():
                        print(f"  - {name}: {detail}")
                    return
            except AttributeError:
                pass
        
        print(f"Function '{function_name}' not found in zar package.")
    
    def __getattr__(self, name):
        return lambda: self.analyze_function(name)

algoWrite = InputAnalyzer()
