from tree import TreeNode


def tree_max_depth(root: TreeNode) -> int:
    def dfs(node) -> int:
        if not node:
            return 0

        return 1 + max(dfs(node.left), dfs(node.right))

    return dfs(root) if root else 0


def main():
    tree = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.from_list(tree)
    result = tree_max_depth(root)
    print(result)

    tree = [1, None, 2]
    root = TreeNode.from_list(tree)
    result = tree_max_depth(root)
    print(result)


if __name__ == "__main__":
    main()
