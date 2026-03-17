from interview.structures.tree import TreeNode


def delete_node(root: TreeNode, key: int) -> TreeNode | None:
    if not root:
        return None

    if key == root.val:
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        curr = root.right
        while curr.left:
            curr = curr.left

        root.val = curr.val
        root.right = delete_node(root.right, curr.val)
        return root

    if key > root.val:
        root.right = delete_node(root.right, key)
    else:
        root.left = delete_node(root.left, key)

    return root


def main():
    tree = [5, 3, 6, 2, 4, None, 7]
    root = TreeNode.from_list(tree)
    root.print()
    result = delete_node(root, 3)
    result.print()


if __name__ == "__main__":
    main()
