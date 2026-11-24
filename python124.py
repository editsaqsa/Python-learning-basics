# Function caching
from functools import lru_cache
import time


@lru_cache(maxsize=None)
def slow_square(n):
    time.sleep(2)
    return n*n


print("1st call (2 sec lagega):" , slow_square(5))
print("2nd call (foran aayega):" , slow_square(5))
print("Cache info:" , slow_square.cache_info())
