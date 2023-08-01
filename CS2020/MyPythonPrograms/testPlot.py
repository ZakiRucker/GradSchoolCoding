import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


x = np.arange(-10, 10, 0.1);
y = np.arctan(x)
plt.plot(x, y)
plt.show()
plt.close("all")
