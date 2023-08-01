import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

G=nx.Graph()
G.add_edges_from([(1,2),(1,3),(3,4)])
nx.draw_random(G)
plt.show()
plt.close("all")