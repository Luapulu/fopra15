import numpy as np
import matplotlib.pyplot as plt


echo_data = np.genfromtxt("echo.txt", delimiter=';', skip_header=14)

plt.plot(echo_data[:, 0], echo_data[:, 2])
plt.xlabel("Time / ns")
plt.ylabel("Average Intensity / count")

plt.savefig("echo.png")

plt.show()
