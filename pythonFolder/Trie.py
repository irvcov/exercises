

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if cur.children.get(c, False) == False:
                nd = TrieNode()
                cur.children[c] = nd
            cur = cur.children[c]
        cur.isEnd = True
            

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if cur.children.get(c, False) == False:
                return False
            cur = cur.children[c]
        return cur.isEnd  

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if cur.children.get(c, False) == False:
                return False
            cur = cur.children[c]
        return True  

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.val = None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)