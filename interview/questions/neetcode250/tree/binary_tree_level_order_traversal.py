from interview.structures.tree import TreeNode
from collections import deque


def level_order_traversal(root):
    result = []
    que = deque([root])
    while que:
        level = []
        for _ in range(len(que)):
            curr = que.popleft()
            level.append(curr.val)

            if curr.left:
                que.append(curr.left)

            if curr.right:
                que.append(curr.right)

        result.append(level)

    return result


def main():
    tree = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.from_list(tree)
    result = level_order_traversal(root)
    val = [[3], [9, 20], [15, 7]]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
