ALPHABET_SIZE = 256  # ASCII size

class TrieNode:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = ''
        self.children = [None] * ALPHABET_SIZE
        self.isEndOfWord = False

class MyTrie:
    # LeetCode 208.Implement Trie (Prefix Tree)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = ''
        self.children = [None] * ALPHABET_SIZE
        self.isEndOfWord = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for alphabet in word:
            node = Trie()
            node.val = alphabet
            cur.children[ord(alphabet)] = node
            cur = node
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for idx, alphabet in enumerate(word):
            node = cur.children[ord(alphabet)]
            if node is None:
                return False
            if node.val != alphabet:
                return False
            if node.isEndOfWord is True and idx != (len(word) - 1):
                return False
            cur = node
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # TODO!
        pass
        # def dfs(node, prefix, result):
        #     if node.isEndOfWord:
        #         return prefix+node.val
        #     for child in node.children:
        #         if child is None:
        #             continue
        #         val = dfs(child, prefix+child.val, result)
            

        # cur = self
        # for alphabet in prefix:
        #     node = cur.children[ord(alphabet)]
        #     if node is None:
        #         return result
        #     cur = node
        # result = []
        # return dfs(cur, prefix, result)

class Trie:
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char,{})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node
    
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
        
obj = Trie()
obj.insert('ow')
obj.insert('owrd')
obj.insert('owhackw')
assert obj.search('ow') == True
assert obj.search('owrw') == False
print(obj.startsWith('ow'))


