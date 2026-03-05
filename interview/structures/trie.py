import json


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def __repr__(self):
        return json.dumps(self.root, indent=4)

    def add(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr:
                curr[ch] = {}

            curr = curr[ch]

        curr[self.end_symbol] = True

    def exists(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr:
                return False

            curr = curr[ch]

        return self.end_symbol in curr

    def suggestions(self, prefix) -> list[str] | None:
        curr = self.root
        for ch in prefix:
            if ch not in curr:
                return None

            curr = curr[ch]

        result = []

        def find(node: dict, pre: str):
            for k, v in node.items():
                if isinstance(v, dict):
                    find(node[k], pre + k)
                    continue

                if k == self.end_symbol:
                    result.append(pre)

        find(curr, prefix)
        return result


def main():
    trie = Trie()
    words = ["hello", "help", "hi"]
    for word in words:
        trie.add(word)

    print(trie)

    print(trie.suggestions("hel"))
    print(trie.exists("hel"))
    print(trie.exists("hello"))


if __name__ == "__main__":
    main()
