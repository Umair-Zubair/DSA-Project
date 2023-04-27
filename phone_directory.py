#making trie 

def make_trie(*words):
    global root
    with open("tst.txt","r") as testing:
        root = testing.read()
        if len(root)!=0:
            root = eval(root)
    if len(words) == 0:
        return "Please enter a name"
    for word in words:
        if not word: 
            continue
        current_dict = root 
        for letter in word:
            if letter not in current_dict:
                current_dict[letter] = {} #aik letter ki aik dict banana
            current_dict = current_dict[letter] #usi letter ke ander aik dict banana
        if letter == word[-1]: #jab end ho iska mtlb letter end hogaya hai aur Flag daaldo 
            current_dict["Flag"] = True 
    with open("tst.txt","w") as out:
        out.write(str(root))
    return root
        
    
# make_trie("Aria", "Ace", "Aspen", "Atlas", "Autumn", "Blaze", "Blue", "Cash", "Clover", "Cruz", "Dahlia", "Diesel", "Eden", "Fox", "Hunter", "Jade", "Jagger", "Kai", "Kingston", "Knox", "Luna", "Levi", "Maverick", "Meadow", "Marley", "Nova", "Ocean", "Onyx", "Orion", "Phoenix", "Poppy", "Raven", "Ruby", "Scarlett", "Skye", "Saffron", "Summer", "Storm", "Violet", "Willow")
# make_trie("Umair")

with open("tst.txt","r") as testing:
    root = eval(testing.read())
#deletion
# print(root)
def delete_from_trie(root, word):
    with open("tst.txt","r") as testing:
        root = eval(testing.read())
    node = root
    parents = [None] * (len(word) + 1)  # keep track of parent nodes
    
    # Traverse the trie to find the node that represents the word to be deleted
    for i, c in enumerate(word):
        if c not in node:
            # Word not found in trie, do nothing
            return
        parents[i] = node #har letter ko aik list mein store krana taake baad mein use kr sakein
        node = node[c] #taake we can reach the flag
    
    # If the 'Flag' key is not in the node, the word is not in the trie, so do nothing
    if 'Flag' not in node:
        return
    
    # Remove the 'Flag' key from the node to signify that the word is no longer in the trie
    del node['Flag']
    
    # Traverse the word in reverse order and remove any nodes that have no children
    for i in range(len(word)-1, -1, -1): #reverse mein chalega 
        if not node and parents[i]: #agr node ki value none hai aur parents mein kuch hai toh krega delete
            # If the current node has no children and is not the root node, remove it
            del parents[i][word[i]]
            node = parents[i]
        else: #agr node none nahi iska mtlb parents[i] wale letter ke bache hain usko na delete kero
            # If the current node has children or is the root node, we're done
            break
    with open("tst.txt","w") as out:
            out.write(str(root))
    

delete_from_trie(root, "Umair")
with open("tst.txt","r") as testing:
    root = eval(testing.read())
# print(root)

# delete_from_trie(root,"Shaaf")


# searching in trie using dfs

# print(root)

# this intial search checks if a word is in trie or not
def search_name(root, word):
    node = root
    for c in word:
        if c not in node:
            return False
        node = node[c]
    return 'Flag' in node


#  this search returns the words the start with a semilar prefix

def search_trie(root, prefix):
    # Traverse the trie to the point where the prefix ends
    node = root
    for c in prefix:
        if c not in node:
            return []
        node = node[c]
    
    # Perform a depth-first search to find all words with the prefix
    results = []
    stack = [(node, prefix)]
    while stack:
        current_dict, current_prefix = stack.pop()
        if 'Flag' in current_dict:
            results.append(current_prefix)
        for letter, child_dict in current_dict.items():
            if letter != 'Flag':
                stack.append((child_dict, current_prefix + letter))
    
    return results



# print(search_trie(root,"S"))
# delete_from_trie(root,"Shaaf")
# print(root)

# print(search_trie(root,"M"))

# "Aria", "Ace", "Aspen", "Atlas", "Autumn", "Blaze", "Blue", "Cash", "Clover", "Cruz", "Dahlia", "Diesel", "Eden", "Fox", "Hunter", "Jade", "Jagger", "Kai", "Kingston", "Knox", "Luna", "Levi", "Maverick", "Meadow", "Marley", "Nova", "Ocean", "Onyx", "Orion", "Phoenix", "Poppy", "Raven", "Ruby", "Scarlett", "Skye", "Saffron", "Summer", "Storm", "Violet", "Willow"


# def Select_Funtion():
#     print("Please select the option from below by typing the number corresponding to it.")
#     print("1. Create a New Contact\n2. Search a Contact.\n3. Delete a Contact.")
#     option = int(input())
#     name = input("Please Enter a Name:")
#     if option == 1:
#         make_trie(name)
#     elif option == 2:
#         print(search_name(root,name))
#     elif option == 3:
#         delete_from_trie(root,name)
#     else:
#         print("Select a Valid Option.")
        
# # Select_Funtion()