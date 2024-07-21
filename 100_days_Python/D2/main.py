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

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def _collect_words(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            self._collect_words(next_node, prefix + char, words)

    def get_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        words = []
        self._collect_words(node, prefix, words)
        return words


# Create a trie
trie = Trie()

# Insert words
trie.insert("bat")
trie.insert("ball")
trie.insert("barn")
trie.insert("basket")
trie.insert("batman")

# Search for words
print(trie.search("bat"))        # True
print(trie.search("ball"))       # True
print(trie.search("basket"))     # True
print(trie.search("base"))       # False

# Check if prefixes exist
print(trie.starts_with("ba"))    # True
print(trie.starts_with("bat"))   # True
print(trie.starts_with("bas"))   # True
print(trie.starts_with("cat"))   # False

# Get all words with a given prefix
print(trie.get_words_with_prefix("ba"))  # ['bat', 'ball', 'barn', 'basket', 'batman']
print(trie.get_words_with_prefix("bat")) # ['bat', 'batman']
print(trie.get_words_with_prefix("bas")) # ['basket']
print(trie.get_words_with_prefix("cat")) # []
