import matplotlib.pyplot as plt

def plotting(title: str, values: list[float], filename="wykres.png"):
    x_axis: list = [x for x in range(len(values))]
    plt.plot(x_axis, values)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

if __name__ == "__main__":
    plotting("test", [4.33, 6.77, 2.55])