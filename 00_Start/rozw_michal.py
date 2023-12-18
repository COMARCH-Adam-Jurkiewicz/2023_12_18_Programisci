lista_przedzialow = []


def przedzial(firstHalf, secondHalf):
    arra = []

    start = 0
    end = 0
    if (firstHalf[0] == '('):
        start = int(firstHalf.split('(')[1]) + 1

    if (firstHalf[0] == '<'):
        start = int(firstHalf.split('<')[1])
        print(start)
    if (secondHalf[len(secondHalf) - 2] == ')'):
        end = int(secondHalf.split(')')[0]) - 1

    if (secondHalf[len(secondHalf) - 2] == '>' or secondHalf[len(secondHalf) - 1] == '>'):
        end = int(secondHalf.split('>')[0])

    for i in range(start, end + 1):
        arra.append(i)

    return arra


with open('przedzialy.txt') as f:
    bigArray = []
    for line in f:
        splitOne = str(line).split(',')[0]
        splitTwo = str(line).split(',')[1]
        array = przedzial(splitOne, splitTwo)
        bigArray.append(array)

print(bigArray)