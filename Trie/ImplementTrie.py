class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        parent = self.root
        for i, ch in enumerate(word):
            if ch not in parent.children:
                newNode = TrieNode(ch)
                parent.children[ch] = newNode
            parent = parent.children[ch]

            if i == len(word) - 1:
                parent.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        parent = self.root
        for ch in word:
            if ch not in parent.children:
                return False
            parent = parent.children[ch]

        return parent.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        parent = self.root
        for ch in prefix:
            if ch not in parent.children:
                return False
            parent = parent.children[ch]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)