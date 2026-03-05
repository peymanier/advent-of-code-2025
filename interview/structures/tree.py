from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, elements):
        root = cls(val=elements[0])

        nodes = [root]
        for i, x in enumerate(elements[1:]):
            if x is None:
                continue

            node = cls(val=x)
            parent_node = nodes[i // 2]

            is_left = i % 2 == 0
            if is_left:
                parent_node.left = node
            else:
                parent_node.right = node

            nodes.append(node)

        return root

    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if self.val == val:
            return

        if val > self.val:
            if self.right is None:
                self.right = TreeNode(val)
                return

            self.right.insert(val)
        else:
            if self.left is None:
                self.left = TreeNode(val)
                return

            self.left.insert(val)

    def delete(self, val):
        if self.val is None:
            return None

        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)

            return self

        elif val < self.val:
            if self.left:
                self.left = self.left.delete(val)

            return self

        if not self.right:
            return self.left

        if not self.left:
            return self.right

        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left

        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)

        return self

    def get_min(self):
        curr = self
        while curr.left:
            curr = curr.left

        return curr.val

    def get_max(self):
        if not self:
            return None

        if not self.right:
            return self.val

        return self.right.get_max()

    def print(self, level=0, label="R"):
        print(f"{level * '  '}{label}> {self.val}")

        if self.left:
            self.left.print(level + 1, label="l")

        if self.right:
            self.right.print(level + 1, label="r")


def level_order_traversal(root: TreeNode) -> list[list[int]]:
    result = []
    queue = deque([root])
    while queue:
        n = len(queue)
        level_vals = []
        for _ in range(n):
            node = queue.popleft()
            level_vals.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level_vals)

    return result


if __name__ == "__main__":
    root = TreeNode(5)
    root.insert(3)
    root.insert(10)
    root.insert(12)
    root.insert(0)
    root.insert(7)
    root.insert(1)
    root.insert(2)
    root.delete(0)

    root.print()
    print("min", TreeNode.get_min(root))
    print("max", TreeNode.get_max(root))
