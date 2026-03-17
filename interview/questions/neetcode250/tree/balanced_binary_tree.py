from interview.structures.tree import TreeNode


def is_balanced_binary_tree(root):
    is_balanced = True

    def dfs(node):
        nonlocal is_balanced
        # acts like a break
        if not is_balanced:
            return 0

        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        if abs(left - right) > 1:
            is_balanced = False

        return 1 + max(dfs(node.left), dfs(node.right))

    dfs(root)
    return is_balanced


def main():
    root = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
    result = is_balanced_binary_tree(root)
    val = True
    print("passed:", result == val, "expected", val, "got", result)

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.left.left.left.left = TreeNode(8)
    result = is_balanced_binary_tree(root)
    val = False
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
