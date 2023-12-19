from icecream import ic
def fn(a=4, b=5, c=10):
    return (a+b)*c

def fn2(a=5, b, c=10):
    return (a+b)*c

ic(fn(2,3,10))
ic(fn(2,3,5))
ic(fn2(b=2,3,a=5))
ic(fn(2,3))
ic(fn(2))
ic(fn())