
# coding: utf-8

# # Challenge Problem 4
# ## Jacob Craffey

# In[4]:

import warnings
warnings.filterwarnings('ignore')

import networkx as nx
import matplotlib.pyplot as plt

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

print ('Global cluster coefficient of network: ' + str(nx.average_clustering(network)))
nx.clustering(network)



# ## Most Central Actor
# 
# The "most central" actor in my network is **George Clooney** with a cluster coefficient of **.61**.
# 
# ## Actor's Cluster Coefficient By Hand
# 
# The five actors that I have chosen to calculate their cluster coefficients by hand are: **Tom Hanks**, **Mel Gibson**, **Russell Crowe**, **Robin Williams** and **Heath Ledger**.
# 
# ### Actor's Node Degree and Values
# 
# 1. **Tom Hanks**'s node **degree** is **6** and his dictionary values are as follows: 
#      - ['Brad Pitt', 'Leonardo DiCaprio', 'Morgan Freeman', 'Bruce Willis', 'Matt Damon', 'Kevin Bacon']. 
# 
# 
# 2. **Mel Gibson**'s node **degree** is **6** and his dictionary values are as follows: 
#      - ['Clint Eastwood', 'Heath Ledger', 'Christian Bale', 'Harrison Ford', 'Liam Neeson', 'Robin Williams'].  
# 
# 
# 3. **Russell Crowe**'s node **degree** is **6** and his dictionary values are as follows: 
#     - ['Kevin Costner', 'Leonardo DiCaprio', 'Kevin Spacey', 'Christian Bale', 'Liam Neeson', 'Will Smith'].  
# 
# 
# 4. **Robin Williams**' node **degree** is **6** and his dictionary values are as follows: 
#     - ['Brad Pitt', 'Mel Gibson', 'Kevin Spacey', 'Christian Bale', 'Matt Damon', 'John Travolta'].  
# 
# 
# 5. **Heath Ledger**'s node **degree** is **6** and his dictionary values are as follows: 
#     - ['Mel Gibson', 'Morgan Freeman', 'Johnny Depp', 'Christian Bale', 'Gary Oldman', 'Matt Damon'].  
# 
# ### Number of Edges Between Neighbors
# 
# 1. **Tom Hanks**.  
#     1. **9 edges**.
#     2. [(Brad Pitt, Leonardo Dicaprio), (Brad Pitt, Morgan Freeman), (Brad Pitt, Bruce Willis), (Brad Pitt, Matt Damon), (Brad Pitt, Kevin Bacon), (Leonardo Dicaprio, Damon), (Morgan Freeman, Bruce Willis), (Morgan Freeman, Matt Damon), (Bruce Willis, Matt Damon)]. 
# 
# 
# 2. **Mel Gibson**
#     1. **6 edges**
#     2. [(Clint Eastwood, Harrison Ford), (Clint Eastwood, Liam Neeson), (Heath Ledger, Christian Bale), (Christian Bale, Liam Neeson), (Christian Bale, Robin Williams), (Harrison Ford, Liam Neeson)].
#     
# 
# 3. **Russell Crowe**
#     1. **3 edges**.
#     2. [(Leonardo Dicaprio, Liam Neeson), (Christian Bale, Liam Neeson), (Liam Neeson, Will Smith)].
#     
# 
# 4. **Robin Williams**
#     1. **7 edges**.
#     2. [(Brad Pitt, Kevin Spacey), (Brad Pitt, Christian Bale), (Brad Pitt, Matt Damon), (Kevin Spacey, Christian Bale), (Mel Gibson, Christian Bale), (Kevin Spacey, Matt Damon), (Matt Damon, John Travolta)].
# 
# 
# 5. **Heath Ledger**
#     1. **8 edges**
#     2. [(Mel Gibson, Christian Bale), (Morgan Freeman, Christian Bale), (Morgan Freeman, Gary Oldman), (Morgan Freeman, Matt Damon), (Johnny Depp, Christian Bale), (Johnny Depp, Matt Damon), (Christian Bale, Gary Oldman)]
#     
# ### Calculations For Cluster Coefficients
#     
# 
# With the equation of cluster coefficient:(2*N<sub>v</sub>) / (K<sub>v</sub>(K<sub>v</sub>-1)) and the appropriate information gathered from each desired actor, we are now able to calculate the cluster coefficient.
# 
# **Tom Hanks**: (2*N<sub>v</sub>) / (K<sub>v</sub>(K<sub>v</sub>-1)) = (2 x 9) / (6(6 - 1)) = **.6**.
# 
# 
# **Mel Gibson**: (2*N<sub>v</sub>) / (K<sub>v</sub>(K<sub>v</sub>-1)) = (2 x 6) / (6(5 - 1)) = **.4**.
# 
# 
# **Russell Crowe**: (2*N<sub>v</sub>) / (K<sub>v</sub>(K<sub>v</sub>-1)) = (2 x 3) / (6(5 - 1)) = **.2**.
# 
# 
# **Robin Williams**: (2*N<sub>v</sub>) / (K<sub>v</sub>(K<sub>v</sub>-1)) = (2 x 7) / (6(5 - 1)) = **.333**.
# 
# **Heath Ledger**: (2*N<sub>v</sub>) / (K<sub>v</sub>(K<sub>v</sub>-1)) = (2 x 8) / (6(5 - 1)) = **.533**.
# 
# 
# 
# 
# 
