from icecream import ic
def fn(*args, **kwargs):
    pass

def fn1(a, b, c):
    return a, b, c
def fn2(*args):
    return args

def fn3(**kwargs):
    return kwargs

def fn4(*args, **kwargs):
    return kwargs, args

ic(fn1(2,3,4))
ic(fn2(2,3,4,5))
ic(fn3(x=2,b=3,cos=4,ayz=5))
ic(fn4(2,3))
ic(fn4(2,3,x=5, rf=4))
# ic(fn4(2,3,x=5, rf=4, 5))
