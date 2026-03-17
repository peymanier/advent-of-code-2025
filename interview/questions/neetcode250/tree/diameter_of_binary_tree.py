from interview.structures.tree import TreeNode


def max_depth_of_binary_tree(root):
    if not root:
        return 0

    return 1 + max(
        max_depth_of_binary_tree(root.left), max_depth_of_binary_tree(root.right)
    )


def diameter_of_binary_tree(root):
    if not root:
        return 0

    result = 0

    def dfs(node):
        if not node:
            return

        nonlocal result
        result = max(
            result,
            max_depth_of_binary_tree(node.left) + max_depth_of_binary_tree(node.right),
        )
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def main():
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(7)
    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(9)
    result = diameter_of_binary_tree(root)
    val = 4
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
