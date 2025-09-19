import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=25)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Гистограмма")
plt.show()