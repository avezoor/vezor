from .gcd import *
from . import gcd
from .prime_list import prime_list
from .min_distance import min_distance

__all__ = ["prime_list","min_distance"]
__submodule__ = {
    "gcd": gcd
    }