# librerías

import networkx as nx
import matplotlib.pyplot as plt
import random as ran
import numpy as np

#---------------------------------------------------------------------------

N=20
def  edgeinfection(G):  #program no hace nada como 
    NaC=ran.randint(0,N)
    G.nodes[NaC]['Estado']='I'
    return G, NaC

#---------------------------------------------------------------------------

G = nx.scale_free_graph(N)
for i in range(N):
    G.nodes[i]['Estado']='S'

color_map={'S': 'green', 'I': 'blue'}
    
plt.figure(num=None, figsize=(8, 6), dpi=80)
pos=nx.circular_layout(G)
nx.draw(G,pos,node_size = 30,)
plt.show()

#---------------------------------------------------------------------------

G,edge=edgeinfection(G)
Graph.neighbors(G)
# nx.draw(G,pos,node_color=[color_map[G.node[node]['Estado']] for node in G], node_size = 30)
nx.draw(G,pos,nodes_color==[color_map[G.nodes[nodes]['Estado']] for nodes_color[color_map[G.nodes[nodes]['Estado']]] in G.edges[',']['blue']])

# nx.draw(G,pos,node_color=[color_map[G.nodes[nodes]['Estado']] for node_color=[color_map[G.nodes[nodes]['Estado']]] in G.edges[,]['blue'])
plt.show()
print(edge)

# for n, nbrsdict in G.adjacency():
# for nbr in G[n]: iterates through neighbors.



# Graph.__iter__(): Iterate over the nodes.

# Graph.neighbors():	Return an iterator over all neighbors of node n.
# Graph.number_of_edges([u, v]): Return the number of edges between two nodes.