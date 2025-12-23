# 前缀树


class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]: # 不存在
                return None
            # 存在，继续
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                # 不存在，创建
                node.children[ch] = Trie()
            # 向下移动
            node = node.children[ch]
        # 标记
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)

        return node is not None and node.isEnd # 前缀存在，且是完整字符串
        

    def startsWith(self, prefix: str) -> bool:
        # 前缀存在即可
        node = self.searchPrefix(prefix)
        return node is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# 每个节点包含
# 指向子节点的指针数组，对本题而言，长度 26，每个元素对应一个字母
# 布尔字段 isEnd，表示该节点是否是字符串结尾
