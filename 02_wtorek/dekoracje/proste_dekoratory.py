# lru_cache - funkcje arytmetyczne
# 23 lub 8.5 sek

from functools import lru_cache
from random import randint as r
from time import time

@lru_cache(maxsize=30000)
def fn_math(a, b, c):
    d = a ** b
    e = a / c
    f = d * e
    return f

start = time()
for _ in range(10000000):
    a, b, c = 10, 20, 30
    # a, b, c = r(1,100), r(1,100), r(1,100)
    x = fn_math(a, b, c)

elapsed = time() - start
print(f"{elapsed=}")