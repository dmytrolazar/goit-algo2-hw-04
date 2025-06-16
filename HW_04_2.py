class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word, value=None):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Input must be a list of strings")

        if not strings:
            return ""

        min_word = min(strings, key=len)
        for i in range(len(min_word)):
            prefix = min_word[:i + 1]
            if not all(word.startswith(prefix) for word in strings):
                return min_word[:i]

        return min_word


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    result = trie.find_longest_common_word(strings)
    print(result)  # Вивід у консоль
    assert result == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    result = trie.find_longest_common_word(strings)
    print(result)  # Вивід у консоль
    assert result == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    result = trie.find_longest_common_word(strings)
    print(result)  # Вивід у консоль
    assert result == ""
