class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        def searchRecursive(index, node):
            cur = node
            for j in range(index, len(word)):
                ch = word[j]
                if ch == '.':
                    for child in cur.children.values():
                        if searchRecursive(j+1, child):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            return cur.end
        return searchRecursive(0, self.root)