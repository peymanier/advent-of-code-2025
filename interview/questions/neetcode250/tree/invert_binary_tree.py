from interview.structures.tree import TreeNode


def invert_binary_tree(root):
    if not root:
        return

    left = root.left
    root.left = root.right
    root.right = left

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return


def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    root.print()
    invert_binary_tree(root)
    root.print()


if __name__ == "__main__":
    main()
