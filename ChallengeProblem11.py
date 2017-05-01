
# coding: utf-8

# # Challenge Problem 11
# ## Jacob Craffey

# In[26]:

def is_reflexive(graph):
    for node in graph:
        if node not in graph[node]:
            return False
    return True

def is_symmetric(graph):
    for node in graph:
        for edge in graph[node]:
            if node not in graph[edge]:
                return False
    return True

def is_antisymmetric(graph):
    for node in graph:
        for edge in graph[node]:
            if node in graph[edge] and node != edge:
                return False
    return True
    
def is_transitive(graph):
    for node in graph:
        for edge in graph[node]:
            for super_edge in graph[edge]:
                if super_edge not in graph[node]:
                    return False
    return True


# ## Description of Code
# ### is_reflexive
# Checks every node and checks if the node is in the values (pointing to itself).  If a node is not pointing to itself, it returns false.  If the loop finishes, all nodes point to itself and returns true.
# 
# ### is_symmetric
# Checks every node and every edge.  If the node's edge value is not in the edge's node list of values (other node does not point back), the graph is not symmetric and returns false.  Nodes that point  If the loop finishes, all nodes have mutual relationships and returns true.
# 
# ## is_antisymmetric
# Recycled code from is_symmetric.  Only difference is if the node's edge value is in the edge's node list of values (other node points back), the graph is not antisymmetric and returns false.  Also, the node and edge must hold differet values.  If the node  If the loop finishes, all nodes have a one-way relationship.  
# 
# ## is_transitive
# Checks all of the nodes' edges and the edges of the parent node.  If a parent's edge value is not found in the child's edge list, the graph is not transitive and returns false.  If the loop completes, all parent's edges are in their children's edge list and returns true.    
