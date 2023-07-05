class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, word):
        current = self.root
        for chr in word:
            node = current.children.get(chr)
            if node == None:
                node = TrieNode()
                current.children.update({chr: node})
            current = node
        current.end_of_string = True
        print("successfully inserted string")

    def search_string(self, word):
        current_node = self.root
        for chr in word:
            node = current_node.children.get(chr)
            if node == None:
                return False
            current_node = node
        if current_node.end_of_string == True:
            return True
        else:
            return False


def delete_string(root, word, index):
    chr = word[index]
    current_node = root.children.get(chr)
    can_this_node_be_deleted = False

    # some prefix is just like others so we should do:
    if len(current_node.children) > 1:
        delete_string(current_node, word, index+1)
        # we will asian the one which comes from delete string
        return False

    # this time we are at the last char  of this word but this one is part of other words
    # we need to just set end of string to False

    # we are at the last word(char):
    if index == len(word) - 1:
        if len(current_node.children) >= 1:
            current_node.end_of_string = False
            return False
        else:
            # if there is nothing then delete
            root.children.pop(chr)
            return True

    if current_node.end_of_string == True:
        delete_string(current_node, word, index+1)
        return False

    can_this_node_be_deleted = delete_string(current_node, word, index+1)
    if can_this_node_be_deleted == True:
        root.children.pop(chr)
        return True
    else:
        return False


new_trie = Trie()

new_trie.insert_string('APP')
new_trie.insert_string('API')
# this is going to be true
print(new_trie.search_string('APP'))
# but this one is just prefix of another word so it's false
print(new_trie.search_string('AP'))

print("================================================================")

delete_string(new_trie.root, "APP", 0)
print(new_trie.search_string('APP'))
