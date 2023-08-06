class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.__root = TrieNode()

    def add(self, word):
        curr = self.__root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True

    def search(self, word):
        def dfs(start, node):
            curr = node
            for i in range(start, len(word)):
                char = word[i]
                if char == '.':
                    for next in curr.children.values():
                        if dfs(i + 1, next):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.isEnd
        return dfs(0, self.__root)