from .sorting import *
from .searching import *
from .geometry import *
from . import geometry
from . import searching
from . import sorting

__all__ = ["algoPrint", "algoWrite", "help"]
__submodule__ = {
    "sorting": sorting,
    "searching": searching,
    "geometry": geometry,
    "formula": formula
    }


from .print import algoPrint
from .write import algoWrite
from .help import help
