def parsuj(*args):
    start_symbol, start, end, end_symbol = args

    start = int(start)
    end = int(end)

    if start_symbol == '(':
        start += 1
    if end_symbol == ')':
        end -= 1

    return list(range(start, end + 1))


lista_przedzialow = []

with open('przedzialy.txt', 'r') as dane:
    for line in dane:
        line = line.strip()
        current_list = parsuj(line[0], *line.strip('()[]<>').split(','), line[-1])
        lista_przedzialow.append(current_list)

print(f"Wynik: {lista_przedzialow=}")