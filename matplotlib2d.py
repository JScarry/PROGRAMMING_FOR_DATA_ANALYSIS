from re import X
import matplotlib.pyplot as plt
import numpy as np
import statistics
import scipy

x = np.arange(0, 10, 0.1)
y = 3 * x

noise = np.random.normal(0.0, 2, len(x))
plt.plot(x, y + noise, '-g.')
plt.plot(x, y)

plt.show()

x = 