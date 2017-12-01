# import pandas as pd
import networkx as nx
# input_data = pd.read_csv('A.csv', index_col=0)
# G = nx.DiGraph(input_data.values)
# nx.draw(G)

# import scipy as sp
# import networkx as nx
# G=nx.fast_gnp_random_graph(100,0.04)
# adj_matrix = nx.adjacency_matrix(G)
# H=nx.Graph(adj_matrix)

import numpy
A=numpy.matrix([[1,1],[2,1]])
G=nx.from_numpy_matrix(A)
print(G.edges)