# Trie

class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]: # Does not exist
                return None
            # Exists, continue
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                # Does not exist, create
                node.children[ch] = Trie()
            # Move down
            node = node.children[ch]
        # Mark
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)

        return node is not None and node.isEnd # Prefix exists, and is a complete string
        

    def startsWith(self, prefix: str) -> bool:
        # Prefix exists is enough
        node = self.searchPrefix(prefix)
        return node is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Each node contains
# Array of pointers to child nodes, length 26 for this problem, each element corresponds to a letter
# Boolean field isEnd, indicating if this node is end of string
