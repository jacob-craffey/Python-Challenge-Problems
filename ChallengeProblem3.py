
# coding: utf-8

# # Challenge Problem 3
# ## Jacob Craffey

# In[126]:

import networkx as nx

def adj_matrix (graph):
    dimension = graph.number_of_nodes()
    matrix = [[0 for x in range(dimension)] for y in range(dimension)]
    for edge in graph.edges():
        matrix[edge[0]][edge[1]] = 1
        matrix[edge[1]][edge[0]] = 1
    return matrix
    
graph = nx.complete_bipartite_graph(2,5)
print(adj_matrix(graph))


# ## Description
# 
# To begin the **adj_matrix** function, it accepts a **graph** argument.  Next an integer **dimension** equals the number of nodes **graph** has to set the dimension of the **matrix**.  **Matrix** is then a nested list which has a list made up of *n* sublists which has *n* elements.  The entire matrix consists of 0s.  
# 
# Next, we have a *for loop* which iterates for every edge in the **graph**'s edge list.  The **edge** finds its appropriate place into the **matrix** and that said location gets marked with a 1.  The **edge**'s values are now swapped within the matrix since both nodes must be connected to one another in a **matrix**.  This repeats for every **edge** in the edgelist in the graph.
# 
# 
