import numpy as np
import matplotlib.pyplot as plt


ramsey_data = np.genfromtxt("ramsey1.txt", delimiter=';', skip_header=14)

plt.plot(ramsey_data[:, 0], ramsey_data[:, 2])
plt.xlabel("Time / ns")
plt.ylabel("Average Intensity / count")

plt.savefig("ramsey.png")

plt.show()