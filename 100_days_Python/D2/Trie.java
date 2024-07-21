import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            node.children.putIfAbsent(ch, new TrieNode());
            node = node.children.get(ch);
        }
        node.isEndOfWord = true;
    }

    public boolean search(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            node = node.children.get(ch);
            if (node == null) {
                return false;
            }
        }
        return node.isEndOfWord;
    }

    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (char ch : prefix.toCharArray()) {
            node = node.children.get(ch);
            if (node == null) {
                return false;
            }
        }
        return true;
    }

    private void collectWords(TrieNode node, String prefix, List<String> words) {
        if (node.isEndOfWord) {
            words.add(prefix);
        }
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            collectWords(entry.getValue(), prefix + entry.getKey(), words);
        }
    }

    public List<String> getWordsWithPrefix(String prefix) {
        TrieNode node = root;
        for (char ch : prefix.toCharArray()) {
            node = node.children.get(ch);
            if (node == null) {
                return new ArrayList<>();
            }
        }
        List<String> words = new ArrayList<>();
        collectWords(node, prefix, words);
        return words;
    }

    public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insert("bat");
        trie.insert("ball");
        trie.insert("barn");
        trie.insert("basket");
        trie.insert("batman");

        // Search for words
        System.out.println(trie.search("bat"));        // true
        System.out.println(trie.search("ball"));       // true
        System.out.println(trie.search("basket"));     // true
        System.out.println(trie.search("base"));       // false

        // Check if prefixes exist
        System.out.println(trie.startsWith("ba"));    // true
        System.out.println(trie.startsWith("bat"));   // true
        System.out.println(trie.startsWith("bas"));   // true
        System.out.println(trie.startsWith("cat"));   // false

        // Get all words with a given prefix
        System.out.println(trie.getWordsWithPrefix("ba"));  // [bat, ball, barn, basket, batman]
        System.out.println(trie.getWordsWithPrefix("bat")); // [bat, batman]
        System.out.println(trie.getWordsWithPrefix("bas")); // [basket]
        System.out.println(trie.getWordsWithPrefix("cat")); // []
    }
}
