from .gcd import *

from . import gcd
from .prime_list import prime_list
from .min_distance import min_distance
from .isPrime import isPrime

__all__ = ["prime_list", "min_distance", "gcd", "isPrime"]
__submodule__ = {
    "gcd": gcd
    }