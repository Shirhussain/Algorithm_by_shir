class Node:
    def __init__(self, value):
        self.value = value
        self.is_word = False
        self.descending = {}


class Trie:
    def __init__(self):
        root = Node('')

    def add(self, word):
        current = self.root
        index = 0

        while index < len(word):
            letter = word[index]
            if letter in current.descending:
                current = current.descending[letter]
            else:
                new_node = Node(letter)
                current.descending[letter] = new_node
                current = new_node
            index += 1

        current.is_word = True

    def is_word(self, word):
        current = self.root
        index = 0

        while index < len(word):
            letter = word[index]

            if letter not in current.descending:
                return False
            else:
                current = current.descending[letter]
            index += 1
        return current.is_word
