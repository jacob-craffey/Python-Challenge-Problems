
# coding: utf-8

# # Challenge Problem 2
# ## Jacob  Craffey
# 
# 
# 
# 
# 

# In[94]:

import networkx as nx
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

def same_letters(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    word1.sort()
    word2.sort()
    for i in range(4):
        if word1[i] != word2[i]:
            return False
    return True

def replace_letter(word1, word2):
    strike = 0
    for i in range(4):
        if word1[i] != word2[i]:
            strike = strike + 1
        if strike == 2:
            return False
    return True

def differences(word1,word2):
    strike = 0
    for i in range(4):
        if word1[i] != word2[i]:
            strike = strike + 1
    return strike
        
def word_graph(words):
    word_dictionary = {}
    for word in words:
        edges = list()
        current_word = word
        for word in words:
            if word == current_word:
                continue
            if replace_letter(word, current_word) == True:
                edges.append(word)
            if differences(word, current_word) == 2 and same_letters(word, current_word) == True:
                edges.append(word)
        word_dictionary[current_word] = edges
    g = nx.Graph(word_dictionary)
    return g
            
words = ['time', 'tame', 'tome', 'mite', 'acme', 'atme', 'itme', 'item', 'acem']
g = word_graph(words)


nx.to_dict_of_lists(g)
nx.draw_circular(g, with_labels=True, node_color="white")
plt.show()


# # Description of Code
# 
# To begin, we assign a collection of 'words' to a list named **words**.  Then we send **words** to the function named **word_graph**.  Once in the **word_graph** we create a **word_dictionary** that will hold a dictionary of the adjacent nodes.
# 
# To begin the actual process, we create a for loop that iterates over every 'word' in **words**.  For every 'word' (key) we iterate through, we need to instantiate a blank list (named **edges**) which holds potential values.  Additonally, we save the current iteration's 'word' to **current_word** so it is able to compare with other 'words' in the list.   
# 
# Next, we create a nested for loop for every 'word' in the list of **words** to compare every 'word' in the list with the **current_word** for potential adjacency.
# 
# If the **current_word** and the compared 'word' are the same, there is no need to compare them to each other and skips the current iteration.
# 
# In order to check the if a word is connected to **current_word**, it must first go through a boolean function named **replace_letter**.  This function accepts the **current_word** and the 'word' it is being compared to.  **Replace_letter** compares each word letter-by-letter and ensures that they are the same.  If there is a difference in letters, it adds a **strike**.  If there is more than one **strike** in the comparison, the function returns false as it does not pass the criteria.  If there is only one **strike**, the function returns true as there is only a one letter difference in the two words.  
# 
# For every 'word' that has a one letter difference when compared to **current_word**, it is appended to the **edges** list and the two words become adjacent.
# 
# Next, back in the function **word_graph**, we compare the two 'words' with two additional functions to see if the words are the same with two swapped letters.  
# 
# We first send the two words to a function called **differences** which compares the two 'words' letter by letter and adds a **strike** for every letter that is not the same.  
# 
# Next, the two words are sent to a function called **same_letters**.  This function sorts the two words alphabetically and if they have the same letters in the same order, then the function returns True.  If there is any difference in the two 'words,' the function returns False.
# 
# For the 'words' to match the criteriea, there must be two **differences** in the 'words.'  And **same_letters** must return True.  If both of the functions return the aforementioned values, then it proves that there are letters that are swapped and the words are adjacent.  
# 
# This process is looped to compare every word with one another and values are added to the **current_word** (key).  Once the main loop is complete, a complete dictionary is complete and is turned into a graph that is returned by the **word_graph**. 

# In[ ]:



