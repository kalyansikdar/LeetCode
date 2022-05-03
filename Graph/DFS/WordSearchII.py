class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False


class TrieTree:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        parent = self.root

        for i, ch in enumerate(word):
            if ch not in parent.children:
                parent.children[ch] = TrieNode(ch)
            parent = parent.children[ch]

            if i == len(word) - 1:
                parent.isWord = True

    def search(self, word):
        parent = self.root

        for ch in word:
            if ch not in parent.children:
                return False
            parent = parent.children[ch]

        return parent.isWord


class Solution:
    def findWords(self, board, words):
        result = []
        Trie = TrieTree()

        for word in words:
            Trie.insert(word)

        root = Trie.root

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, "", result)

        return result

    def dfs(self, board, i, j, root, resTillNow, result):
        if root.isWord:
            result.append(resTillNow)
            root.isWord = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        ch = board[i][j]

        root = root.children.get(ch)

        if not root:
            return False

        board[i][j] = ''

        self.dfs(board, i + 1, j, root, resTillNow + ch, result)
        self.dfs(board, i - 1, j, root, resTillNow + ch, result)
        self.dfs(board, i, j + 1, root, resTillNow + ch, result)
        self.dfs(board, i, j - 1, root, resTillNow + ch, result)

        board[i][j] = ch


solution = Solution()
board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]

words = ["oath","pea","eat","rain"]
result = solution.findWords(board, words)
print (result)