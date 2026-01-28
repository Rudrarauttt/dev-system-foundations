
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True
    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children: return False
            curr = curr.children[ch]
        return curr.is_end
    def starts_with(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children: return False
            curr = curr.children[ch]
        return True

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True
    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children: return False
            curr = curr.children[ch]
        return curr.is_end
    def starts_with(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children: return False
            curr = curr.children[ch]
        return True
# Implementation of trie
# Last updated: 2026-01-28T21:19:39
# Complexity: O(log N) or O(1)

def trie_operation(x):
    '''Execution routine for trie'''
    return x * 2

