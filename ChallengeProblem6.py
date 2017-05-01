
# coding: utf-8

# # Challenge Problem 6
# ## Jacob Craffey

# In[235]:

import warnings
warnings.filterwarnings('ignore')

import networkx as nx
import matplotlib.pyplot as plt

def sum_of_distance(current_actor):
    sum = 0
    for actor in network:
        if actor == current_actor:
            continue
        sum += len(nx.shortest_path(network,source = current_actor, target = actor)) - 1
    return sum

network = nx.Graph({'Tom Hanks': ['Brad Pitt', 'Leonardo DiCaprio', 'Morgan Freeman', 'Bruce Willis', 'Matt Damon', 'Kevin Bacon'],
                   'Brad Pitt': ['Tom Hanks', 'Leonardo DiCaprio', 'Samuel L. Jackson', 'Kevin Spacey', 'Morgan Freeman', 'Bruce Willis', 'Tom Cruise', 'Christian Bale', 'George Clooney', 'Gary Oldman', 'Harrison Ford', 'Matt Damon', 'Robin Williams', 'Kevin Bacon', 'Jared Leto'],
                    'Kevin Costner': ['Clint Eastwood', 'Tommy Lee Jones', 'Morgan Freeman', 'Russell Crowe', 'Sean Connery', 'Gary Oldman', 'Matt Damon', 'Kevin Bacon', 'John C. Reilly'],
                    'Clint Eastwood': ['Kevin Costner', 'Leonardo DiCaprio', 'Mel Gibson', 'Tommy Lee Jones', 'Morgan Freeman', 'Johnny Depp', 'Harrison Ford', 'Matt Damon', 'Liam Neeson', 'John Travolta'],
                    'Leonardo DiCaprio': ['Tom Hanks', 'Brad Pitt', 'Clint Eastwood', 'Samuel L. Jackson', 'Russell Crowe', 'Johnny Depp', 'Matt Damon', 'Liam Neeson', 'John Travolta', 'Alec Baldwin', 'John C. Reilly'],
                    'Mel Gibson': ['Clint Eastwood', 'Heath Ledger', 'Christian Bale', 'Harrison Ford', 'Liam Neeson', 'Robin Williams'],
                    'Samuel L. Jackson': ['Brad Pitt', 'Leonardo DiCaprio', 'Tommy Lee Jones', 'Kevin Spacey', 'Nicolas Cage', 'Bruce Willis', 'Christian Bale', 'George Clooney', 'Gary Oldman', 'Harrison Ford', 'Liam Neeson', 'John Travolta', 'John C. Reilly'],
                    'Tommy Lee Jones': ['Kevin Costner', 'Clint Eastwood', 'Samuel L. Jackson', 'Nicolas Cage', 'Gary Oldman', 'Harrison Ford', 'Matt Damon', 'Will Smith', 'Kevin Bacon', 'John C. Reilly'],
                    'Kevin Spacey': ['Brad Pitt', 'Samuel L. Jackson', 'Morgan Freeman', 'Russell Crowe', 'Tom Cruise', 'George Clooney', 'Gary Oldman', 'Harrison Ford', 'Matt Damon', 'Robin Williams', 'John Travolta', 'Alec Baldwin'],
                    'Nicolas Cage': ['Samuel L. Jackson', 'Tommy Lee Jones', 'Bruce Willis', 'Christian Bale', 'Sean Connery', 'Will Smith', 'Jared Leto', 'John Travolta'],
                    'Morgan Freeman': ['Tom Hanks', 'Kevin Costner', 'Brad Pitt', 'Clint Eastwood', 'Kevin Spacey', 'Bruce Willis', 'Johnny Depp', 'Tom Cruise', 'Heath Ledger', 'Christian Bale', 'Sean Connery', 'Gary Oldman', 'Matt Damon', 'Liam Neeson'],
                    'Russell Crowe': ['Kevin Costner', 'Leonardo DiCaprio', 'Kevin Spacey', 'Christian Bale', 'Liam Neeson', 'Will Smith'],
                    'Bruce Willis': ['Tom Hanks', 'Brad Pitt', 'Samuel L. Jackson', 'Nicolas Cage', 'Morgan Freeman', 'George Clooney', 'Gary Oldman', 'Matt Damon', 'John Travolta', 'Alec Baldwin'],
                    'Johnny Depp': ['Clint Eastwood', 'Leonardo DiCaprio', 'Morgan Freeman', 'Heath Ledger', 'Christian Bale', 'Matt Damon', 'Kevin Bacon', 'John Travolta', 'John C. Reilly'],
                    'Tom Cruise': ['Brad Pitt', 'Kevin Spacey', 'Morgan Freeman', 'Kevin Bacon', 'John Travolta', 'Alec Baldwin', 'John C. Reilly'],
                    'Heath Ledger': ['Mel Gibson', 'Morgan Freeman', 'Johnny Depp', 'Christian Bale', 'Gary Oldman', 'Matt Damon'],
                    'Christian Bale':['Brad Pitt', 'Mel Gibson', 'Samuel L. Jackson', 'Nicolas Cage', 'Morgan Freeman', 'Russell Crowe', 'Johnny Depp', 'Heath Ledger', 'Gary Oldman', 'Liam Neeson', 'Robin Williams', 'Jared Leto'],
                    'George Clooney': ['Brad Pitt', 'Samuel L. Jackson', 'Kevin Spacey', 'Bruce Willis', 'Gary Oldman', 'Matt Damon', 'Jared Leto', 'John Travolta', 'John C. Reilly'],
                    'Sean Connery': ['Kevin Costner', 'Nicolas Cage', 'Morgan Freeman', 'Harrison Ford', 'Matt Damon', 'Alec Baldwin'],
                    'Gary Oldman': ['Kevin Costner', 'Brad Pitt', 'Samuel L. Jackson', 'Tommy Lee Jones', 'Kevin Spacey', 'Morgan Freeman', 'Bruce Willis', 'Heath Ledger', 'Christian Bale', 'George Clooney', 'Harrison Ford', 'Liam Neeson', 'Kevin Bacon', 'John C. Reilly'],
                    'Harrison Ford': ['Brad Pitt', 'Clint Eastwood', 'Mel Gibson', 'Samuel L. Jackson', 'Tommy Lee Jones', 'Kevin Spacey', 'Sean Connery', 'Gary Oldman', 'Liam Neeson', 'Will Smith', 'Alec Baldwin', 'John C. Reilly'],
                    'Matt Damon': ['Tom Hanks', 'Kevin Costner', 'Brad Pitt', 'Clint Eastwood', 'Leonardo DiCaprio', 'Tommy Lee Jones', 'Kevin Spacey', 'Morgan Freeman', 'Bruce Willis', 'Johnny Depp', 'Heath Ledger', 'George Clooney', 'Sean Connery', 'Will Smith', 'Robin Williams', 'John Travolta', 'Alec Baldwin'],
                    'Liam Neeson': ['Clint Eastwood', 'Leonardo DiCaprio', 'Mel Gibson', 'Samuel L. Jackson', 'Morgan Freeman', 'Russell Crowe', 'Christian Bale', 'Gary Oldman', 'Harrison Ford', 'Will Smith', 'John C. Reilly'],
                    'Will Smith': ['Tommy Lee Jones', 'Nicolas Cage', 'Russell Crowe', 'Harrison Ford', 'Matt Damon', 'Liam Neeson', 'Jared Leto', 'John Travolta', 'Alec Baldwin', 'John C. Reilly'],
                    'Robin Williams': ['Brad Pitt', 'Mel Gibson', 'Kevin Spacey', 'Christian Bale', 'Matt Damon', 'John Travolta'],
                    'Kevin Bacon': ['Tom Hanks', 'Kevin Costner', 'Brad Pitt', 'Tommy Lee Jones', 'Johnny Depp', 'Tom Cruise', 'Gary Oldman', 'Alec Baldwin', 'John C. Reilly'],
                    'Jared Leto': ['Brad Pitt', 'Nicolas Cage', 'Christian Bale', 'George Clooney', 'Will Smith', 'John Travolta', 'John C. Reilly'],
                    'John Travolta': ['Clint Eastwood', 'Leonardo DiCaprio', 'Samuel L. Jackson', 'Kevin Spacey', 'Nicolas Cage', 'Bruce Willis', 'Johnny Depp', 'Tom Cruise', 'George Clooney', 'Matt Damon', 'Will Smith', 'Robin Williams', 'Jared Leto', 'John C. Reilly'],
                    'Alec Baldwin': ['Leonardo DiCaprio', 'Kevin Spacey', 'Bruce Willis', 'Tom Cruise', 'Sean Connery', 'Harrison Ford', 'Matt Damon', 'Will Smith', 'Kevin Bacon', 'John C. Reilly'],
                    'John C. Reilly': ['Kevin Costner', 'Leonardo DiCaprio', 'Samuel L. Jackson', 'Tommy Lee Jones', 'Johnny Depp', 'Tom Cruise', 'George Clooney', 'Gary Oldman', 'Harrison Ford', 'Liam Neeson', 'Will Smith', 'Kevin Bacon', 'Jared Leto', 'John Travolta', 'Alec Baldwin'],
                   })

nx.draw_circular(network, iteration = 9999, node_size = 1000, with_labels = True, node_color="white")
plt.show()


# ## Degree Centrality
# 
# $$ \frac{deg(v)}{n-1} $$
# 
# 1. **Liam Neeson** degree = 11
# $$ \frac{11}{30-1} $$
#     
# $$ =.37931 $$   
# 
# 2. **Will Smith** degree = 10
# $$ \frac{10}{30-1} $$
#     
# $$ =.344827 $$  
# 
# 3. **Mel Gibson** degree = 6
# $$ \frac{6}{30-1} $$
#     
# $$ =.206896 $$ 
# 
# In order to find the degree centrality for these three actors, I found their degree and divided it by the number of nodes in the graph minus 1.

# In[236]:

print(sum_of_distance('Liam Neeson'))
print(sum_of_distance('Will Smith'))
print(sum_of_distance('Mel Gibson'))


# ## Closeness Centrality
# 
# $$ \frac{n-1}{\sum_{i\not{=}j}d(i,j)} $$
# 
# 1. **Liam Neeson** sum of distance = 47
# $$ \frac{30-1}{47} $$
# 
# $$ = .61702 $$
# 
# 2. **Will Smith** sum of distance = 48
# $$ \frac{30-1}{48} $$
# 
# $$ = .6041667 $$
# 
# 3. **Mel Gibson** sum of distance = 57
# $$ \frac{30-1}{57} $$
# 
# $$ = .508772 $$
# 
# For calculating the closeness centrality for a certain actor, I wrote a quick python function that calculates the sum of distance between the desired actor and all other actors in the graph.  Once I found the sum of distance, that divides 29 (30 actors minus 1) and the closeness centrality for that actor is found.

# ## NetworkX Degree Centrality

# In[237]:

print(nx.degree_centrality(network))


# ## NetworkX Betweenness Centrality

# In[238]:

print(nx.betweenness_centrality(network))


# ## NetworkX Closeness Centrality 

# In[239]:

print(nx.closeness_centrality(network))


# ## Highest Centrality Actors
# 
# The actor with the highest **degree centrality** is **Matt Damon** with a closeness centrality of **.586206**.
# 
# The actor with the highest **betweenness centrality** is **Brad Pitt** with a closeness centrality of **.051602**.
# 
# The actor with the highest **closeness cetrality** is **Matt Damon** with a closeness centrality of **.70731**.

# ## Discussion of Results
# 
# There are a lot of ways to express which node is the most important in the graph of actors.  From the results, we could say that:
# 1. **Matt Damon** is the most important person because he has the greatest amount of appearences with other actors in the graph (17).
# 2. **Brad Pitt** is the most important person because he connects to large clusters of actors together.  This means that he starred in two movies that included the largest two portions of my 30 actors.
# 3. **Matt Damon** is the most important because he is the closest (in terms of path length) to the most people.  This means that on average, Matt Damon has appeared in movies with most of the actors in the network or have costars that have worked with other actors in other movies.
# 
# If **Matt Damon's** degree centrality increases or decreases, then Damon has starred in more movies with other actors in the network.  Damon's degree centrality decreases if there are additional actors that are brought into the network that have not been in a movie with Damon.
# 
# If **Brad Pitt's** betweenness centrality increases, then Pitt appears in two movie casts (cluster) of actors that are in the network.  Pitt's betweenness centrality would decrease if there are less actors in the network and they have not been in a movie with Pitt.
# 
# If **Matt Damon's** closeness centrality increases, then Damon will act in a movie actors in my network or have costars that have worked with other actors that have not worked with the Damon.  Damon's closeness centrality would decrease if there were more actors in my network that have not been in a movie with Damon.
