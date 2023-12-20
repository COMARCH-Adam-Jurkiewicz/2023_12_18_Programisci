import matplotlib.pyplot as plt

X = [x for x in range(-100,100)]
Y = [x**2 for x in X ]
plt.plot(X,Y)
plt.grid(True)
plt.title("To jest wykres")
plt.show()