
# coding: utf-8

# # Challenge Problem 12
# ## Jacob Craffey

# In[93]:

def remove_duplicates(composition):
    flatten = {}
    for node in composition:
        for edge in composition[node]:
            if type(edge) is list:
                edgelist = []
                edgelist.extend(edge)
                flatten[node] = edgelist
            else:
                flatten[node].append(edge)
    for node in flatten:
        flatten[node] = list(set(flatten[node]))
    return flatten

def add_edge(composition, relation1, node, edge):
    for i in relation1[edge]:
        if i in composition[node]:
            continue
        composition[node].append(i)
    return composition[node]

def compose(relation1, relation2):
    composition = {}
    for node in relation2:
        for edge in relation2[node]:
            if edge in relation1:
                if node in composition:
                    composition[node] = add_edge(composition, relation1, node, edge)
                else:
                    temp_list = []
                    temp_list.append(relation1[edge])
                    composition[node] = temp_list
    composition = remove_duplicates(composition)
    # Checks for empty lists in relation2
    for node in relation2:
        if not relation2[node]:
            composition[node] = []
    return composition



# ## Description of Code
# To begin, the two relations are read into the **compose** function.  A dictionary named **composition** is created which will eventually contain our answer.  We loop through every key and value in the second relation (if a key has no values, composition creates a blank key).  
# 
# Next, if any of the **relation1** keys contain a **relation2** edge, the composition will write **relation2**'s current key and add **relation1**'s value.
# 
# Currently, there could be duplicate values in the **composition**.  So the dictionary is sent to the **remove_duplicates**.  We loop through **composition**'s keys and for every value 'list', we convert it to a set and then back to a list in order to remove any duplicate values.  The finished composition is then returned through **compose**. 
