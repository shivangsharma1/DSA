class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]
        cur.word = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            c = cur.children[c]

        return True
    
    def prefix(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]

        return True