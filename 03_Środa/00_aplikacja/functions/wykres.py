import matplotlib.pyplot as plt

def plotting(title: str, values: list[float], legenda_wykres: str, leg_x: str, leg_y: str, filename="wykres.png"):
    x_axis: list = [x for x in range(len(values))]
    plt.plot(x_axis, values)
    plt.title(title)
    plt.legend([legenda_wykres])
    plt.xlabel(leg_x)
    plt.ylabel(leg_y)
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

if __name__ == "__main__":
    legenda_wykres = "Waluta XYZ"
    leg_x, leg_y = "Legenda X", "Legenda Y"
    plotting("TEST", [4.33, 6.77, 2.55], legenda_wykres, leg_x, leg_y)
