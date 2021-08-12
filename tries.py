class TrieNode:
    def __init__(self):
        self.next = dict()
        self.word = ""


class Tries:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        temp = self.root
        for c in word:
            if c not in temp.next:
                temp.next[c] = TrieNode()
            temp = temp.next[c]
        temp.word = word

    def search(self, word):
        node = self.search_prefix(word)
        if node is None:
            return False
        return node.word == word

    def search_prefix(self, prefix):
        temp = self.root
        for c in prefix:
            if c not in temp.next:
                return None
            temp = temp.next[c]
        return temp
