import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(500)
y = np.random.rand(500)

plt.scatter(x, y)
plt.xlabel("randX")
plt.ylabel("randY")
plt.title("Диаграмма рассеяния")
plt.show()