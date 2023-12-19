class Test:
    pass

test1 = Test()
test2 = Test()

test1.a = 10
test1.b = 4.34
print(f"{id(test1)=}")
print(f"{id(test2)=}")
print("++++++++++++++++++++++++++")

def fn01():
    print(f"f01->{id(test1)=}")
    print(test1.a)

def fn02():
    print(f"f02->{id(test2)=}")
    test2.a = "AAAA"
    print(test2.a)

def fn03():
    print(f"f03->{id(test1)=}")
    print(f"f03->{id(test2)=}")
    print(dir(test1))
    print("----")
    print(dir(test2))

fn01()
fn02()
fn03()

