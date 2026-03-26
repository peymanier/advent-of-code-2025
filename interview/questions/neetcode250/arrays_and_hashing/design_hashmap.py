class ListNode:
    def __init__(self, key=-1, val=-1, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt


class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def hash(self, key: int):
        return key % len(self.map)

    def put(self, key: int, val: int) -> None:
        index = self.hash(key)
        curr = self.map[index]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = val
                return

            curr = curr.next

        curr.next = ListNode(key=key, val=val)

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.map[index].next
        while curr:
            if curr.key == key:
                return curr.val

            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.map[index]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return

            curr = curr.next


def main():
    hashmap = MyHashMap()
    for i in range(1, 10_001):
        hashmap.put(i, i * 2)

    print(hashmap.get(100))
    print(hashmap.get(1000))
    print(hashmap.get(10000))

    print(hashmap.get(500))
    print(hashmap.remove(500))
    print(hashmap.get(500))


if __name__ == "__main__":
    main()
