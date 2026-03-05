class Hashmap:
    def __init__(self, size):
        self.size = size
        self.hashmap = [None for _ in range(self.size)]

    def key_to_index(self, key):
        result = 0
        for c in key:
            result += ord(c)

        return result % self.size

    def insert(self, key, value):
        self.hashmap[self.key_to_index(key)] = (key, value)

    def get(self, key):
        result = self.hashmap[self.key_to_index(key)]
        if not result:
            raise KeyError

        return result[1]


def main():
    hm = Hashmap(size=10)
    dc = {"peyman": "hello", "this is it": 22, "really": "yes"}
    for k, v in dc.items():
        hm.insert(k, v)

    for k in dc:
        print(hm.get(k))


if __name__ == "__main__":
    main()
