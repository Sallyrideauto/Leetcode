class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    def search_prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                break
            prefix += char
            node = node.children[char]
            if node.is_end_of_word:
                return prefix
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
            
        words = sentence.split()
        replaced_words = []
        for word in words:
            replaced_words.append(trie.search_prefix(word))
        
        return " ".join(replaced_words)