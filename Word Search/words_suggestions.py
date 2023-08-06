import Add_Search

if __name__ == "__main__":
    trie = Add_Search.Trie()
    words = ["bad","dad","mad","pad"]
    for word in words:
        trie.add(word)
    print(trie.search("bad"))
    print(trie.search("b.."))
    print(trie.search(".a."))
