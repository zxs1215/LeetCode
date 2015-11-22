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
        check = self.check_it(word,True)
        check.has_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        check = self.check_it(word)
        return  check != None and  check.has_word  
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.check_it(prefix) != None
        
    def check_it(self, word, add = False):
        check = self.root
        for ch in word:
            node = check.next(ch)
            if node == None:
                if add:
                    node = TrieNode()
                    node.val = ch
                    check.children.append(node)
                else:
                    return None
            check = node
        return check