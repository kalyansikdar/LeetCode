class TrieNode:
    def __init__(self, val):
        self.val = val
        self.count = 0  # counts the occurence of the char
        self.endsHere = 0  # add 1 if a word ends
        self.children = {}


class Trie:

    def __init__(self):
        # initialize the tree with '/' root value
        self.root = TrieNode('/')

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            # if char is not among children, create a new child/node
            if curr.children.get(ch) == None:
                curr.children[ch] = TrieNode(ch)

            # increase the occurrence of the char
            curr.children[ch].count += 1
            # move pointer to descend to the children
            curr = curr.children[ch]

        # mark the word end here. value > 1 means more words end.
        curr.endsHere += 1

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            # if the char is not among the children, word is not available, return false
            if curr.children.get(ch) == None:
                return False

            curr = curr.children[ch]
        # returns true only if a word ends here
        return curr.endsHere > 0

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            # if char not among children, prefix is not available
            if curr.children.get(ch) == None:
                return False

            curr = curr.children[ch]

        # if control comes here, prefix is found, you can just return True
        # return True   # WORKS
        # but in case words can be deleted, then count will be deducted.
        # in those case, you need to check the count value of the node
        # return True if the count is greater than 0
        return curr.count > 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)