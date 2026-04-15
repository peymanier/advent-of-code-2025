class Trie:
    def __init__(self):
        self.store = {}

    def insert(self, word: str) -> None:
        curr = self.store
        for ch in word:
            if ch not in curr:
                curr[ch] = {}

            curr = curr[ch]

        curr["is_word"] = True

    def search(self, word: str) -> bool:
        curr = self.store
        for ch in word:
            if ch not in curr:
                return False

            curr = curr[ch]

        return curr.get("is_word", False)

    def starts_with(self, word: str) -> bool:
        curr = self.store
        for ch in word:
            if ch not in curr:
                return False

            curr = curr[ch]

        return True


def main():
    trie = Trie()
    trie.insert("apple")

    got = trie.search("apple")
    expected = True
    print("passed:", expected == got, "expected", expected, "got", got)

    got = trie.search("app")
    expected = False
    print("passed:", expected == got, "expected", expected, "got", got)

    got = trie.starts_with("app")
    expected = True
    print("passed:", expected == got, "expected", expected, "got", got)

    trie.insert("app")

    got = trie.search("app")
    expected = True
    print("passed:", expected == got, "expected", expected, "got", got)


if __name__ == "__main__":
    main()
