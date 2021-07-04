import numpy as np
import matplotlib.pyplot as plt


rabi_data = np.genfromtxt("rabi.txt", delimiter=';', skip_header=14)

plt.plot(rabi_data[:, 0], rabi_data[:, 2])
plt.xlabel("Time / ns")
plt.ylabel("Average Intensity / count")

plt.savefig("rabi.png")

plt.show()