class ListNode:
    def __init__(self, val: int = -1, nxt=None):
        self.val = val
        self.next = nxt


class MyHashSet:
    def __init__(self):
        self.set = [ListNode() for _ in range(1000)]

    def hash(self, val: int):
        return val % len(self.set)

    def add(self, val: int):
        index = self.hash(val)
        curr = self.set[index]
        while curr.next:
            if curr.next.val == val:
                return

            curr = curr.next

        curr.next = ListNode(val)

    def contains(self, val: int) -> bool:
        index = self.hash(val)
        curr = self.set[index].next
        while curr:
            if curr.val == val:
                return True

            curr = curr.next

        return False

    def remove(self, val: int):
        index = self.hash(val)
        curr = self.set[index]
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return

            curr = curr.next

        return


def main():
    hashset = MyHashSet()
    for i in range(1, 10_001):
        hashset.add(i)

    print(hashset.contains(100))
    print(hashset.contains(1000))
    print(hashset.contains(10000))

    print(hashset.contains(500))
    print(hashset.remove(500))
    print(hashset.contains(500))


if __name__ == "__main__":
    main()
