"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""
import collections

class TrieNode:
    def __init__(self):
    # Initialize your data structure here.
        self.children = collections.OrderedDict()
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for letters in word:
            child = node.children.get(letters)
            if child is None:
                child = TrieNode()
                node.children[letters] = child
            node = child
        node.isWord = True
    
  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for letters in word:
            node = node.children.get(letters)
            if node is None:
                return False
        return node.isWord
        
  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for letters in prefix:
            node = node.children.get(letters)
            if node is None:
                return False
        return True
