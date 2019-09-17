import numpy as np

mu, sigma = 30, 10  # mean and standard deviation
s = np.random.normal(mu, sigma, 10)
print(s)

import matplotlib
matplotlib.use('TkAgg')
print(matplotlib.get_backend())
import matplotlib.pyplot as plt

plt.figure()
plt.interactive(False)
plt.hist(s)


plt.title("test plot")

plt.show(block=True)
plt.interactive(False)


