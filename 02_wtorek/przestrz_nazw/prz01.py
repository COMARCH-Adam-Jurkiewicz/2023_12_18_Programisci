wart_1 = 20
print(f"1->{id(wart_1)=}")

wart_1 = float(wart_1)
print(f"1f->{id(wart_1)=}")

def fn01():
    print(wart_1)
    print(f"01->{id(wart_1)=}")

def fn02():
    wart_1 = 10
    print(wart_1)
    print(f"02->{id(wart_1)=}")

fn02()
fn01()