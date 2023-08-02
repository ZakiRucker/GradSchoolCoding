#author: Arijit with help from the web
#contributing programmers whose code I have reviewed: Alex, Stephen, Lily, Scott

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import csv
import random

#This dictionary will have the key value pairs to map node #s to names.
GraphNodenames={}

# reading the data for each group

with open('GraphConnect.csv', 'r') as csvfile:
  GraphReader = csv.reader(csvfile, delimiter='|')
  for row in GraphReader:
    GraphNodenames[int(row[0])-1]=row[1] #-1 is because the csv has numbers starting from 1 and the dictionary starts from 0

# generate a random graph of 5 nodes and average connectivity 2
Gba=nx.barabasi_albert_graph(5,2)

GbaNodes= Gba.nodes() # get the nodes into a list
print GbaNodes
GbaNodes = map(lambda x:GraphNodenames[int(x)] , GbaNodes) # map the node #s to names 
print GbaNodes


GbaEdges= Gba.edges() # get the edges of the graph
print GbaEdges

#The following complicated logic makes the edges (pair of nodes) into names.
edges1=[]
GbaEdges2=[]
for i in range(len(GbaEdges)):
  edges2=[]
  edges1=list(GbaEdges.pop())
  edges1.reverse()
  edges2.append(GraphNodenames.get(edges1.pop()))
  edges2.append(GraphNodenames.get(edges1.pop()))
  GbaEdges2.append(edges2)
print GbaEdges2

Ger=nx.erdos_renyi_graph(5,3) # generate the 2nd random graph

# map nodes #s to names
GerNodes= Ger.nodes()
print GerNodes
GerNodes = map(lambda x:GraphNodenames[int(x)+5] , GerNodes)
print GerNodes

# get the edges, which are tuples or pairs of 2 nodes
GerEdges= Ger.edges()
print GerEdges

#makes the edgs from numbers to names
edges1=[]
GerEdges2=[]
for i in range(len(GerEdges)):
  edges2=[]
  edges1=list(GerEdges.pop())
  edges1.reverse()
  edges2.append(GraphNodenames.get(edges1.pop()+5))
  edges2.append(GraphNodenames.get(edges1.pop()+5))
  GerEdges2.append(edges2)
print GerEdges2

#now figure out random nodes from each graph to join
#at this point the #s are names in the graph
GbaNodesRandom=random.sample(GbaNodes,3);
GerNodesRandom=random.sample(GerNodes,2);
GbaGerEdges = [(x,y) for x in GbaNodesRandom for y in GerNodesRandom]

#start the process of building one single graph containing the 2 random graphs and interconnections
G=nx.Graph()

#add the nodes and edges from the 2 random graphs and the interconnections
G.add_nodes_from(GbaNodes)
G.add_edges_from(GbaEdges2)
G.add_nodes_from(GerNodes )
G.add_edges_from(GerEdges2 )
G.add_edges_from(GbaGerEdges)

#draw out with nice colors and sizing to make it visually appealing
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,with_labels = True,nodelist=GbaNodes,node_color='cyan', node_size=1500)
nx.draw_networkx_nodes(G,pos,with_labels = True,nodelist=GerNodes,node_color='orange', node_size=1500)
nx.draw_networkx_edges(G,pos,edgelist=GbaEdges2,edge_color='cyan',width=5)
nx.draw_networkx_edges(G,pos,edgelist=GerEdges2,edge_color='orange', width=5)
nx.draw_networkx_edges(G,pos,edgelist=GbaGerEdges,edge_color='r',width=5)
nx.draw_networkx_labels(G,pos,font_color='black',font_weight='bold')


#plotting and display
plt.axis('off') # turn plt axis off (default on)
plt.show()
plt.close("all")


