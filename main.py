import numpy as np
import matplotlib.pyplot as plt

zf_data = np.genfromtxt("frequenzsweep.txt", delimiter=';', skip_header=14)

zf_omega = min(zip(zf_data[:, 1], zf_data[:, 3]), key=lambda t: t[1])[0]

print(zf_omega)

plt.scatter(zf_data[:, 1], zf_data[:, 3])
plt.show()
