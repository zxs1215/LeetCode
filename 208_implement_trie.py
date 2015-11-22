class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.children = []
        self.has_word = False

    def next(self, val):
        for child in self.children:
            if child.val == val:
                return child
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        check = self.root
        for ch in word:
            ne = check.next(ch)
            if ne != None:
                check = ne
            else:
                node = TrieNode()
                node.val = ch
                check.children.append(node)
                check = node
        check.has_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        check = self.root
        for ch in word:
            ne = check.next(ch)
            if ne == None:
                return False
            check = ne
        return check.has_word   
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        check = self.root
        for ch in prefix:
            node = check.next(ch)
            if node == None:
                return False
            check = node
        return True