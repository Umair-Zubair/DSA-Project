

#making trie 
root = {}
def make_trie(*words):
    global root
    if len(words) == 0:
        return "Please enter a name"
    for word in words:
        if not word: 
            continue
        current_dict = root 
        for letter in word:
            if letter not in current_dict:
                current_dict[letter] = {}
            current_dict = current_dict[letter]
        if letter == word[-1]:
            current_dict["Flag"] = True 
    return root
    
make_trie("Shaaf","Murtajiz","Moogi","Umair","Shafique")

#deletion

def delete_from_trie(root, word):
    node = root
    parents = [None] * (len(word) + 1)  # keep track of parent nodes
    
    # Traverse the trie to find the node that represents the word to be deleted
    for i, c in enumerate(word):
        if c not in node:
            # Word not found in trie, do nothing
            return
        parents[i] = node
        node = node[c]
    
    # If the '$' key is not in the node, the word is not in the trie, so do nothing
    if 'Flag' not in node:
        return
    
    # Remove the '$' key from the node to signify that the word is no longer in the trie
    del node['Flag']
    
    # Traverse the word in reverse order and remove any nodes that have no children
    for i in range(len(word)-1, -1, -1):
        if not node and parents[i]:
            # If the current node has no children and is not the root node, remove it
            del parents[i][word[i]]
            node = parents[i]
        else:
            # If the current node has children or is the root node, we're done
            break



delete_from_trie(root,"Shaaf")
# delete_from_trie("Shafique")

# searching in trie using dfs

print(root)

def search_trie(root, word):
    node = root
    for c in word:
        if c not in node:
            return False
        node = node[c]
    return 'Flag' in node


print(search_trie(root,"Shaaf"))