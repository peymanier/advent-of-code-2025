from interview.structures.tree import TreeNode


def inorder_traversal(root):
    result = []

    def traverse(node):
        if not node:
            return

        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
        return

    traverse(root)
    return result


def inorder_traversal_iter(root):
    result = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result


def main():
    root = TreeNode.from_list([1, None, 2, 3])
    result = inorder_traversal(root)
    val = [1, 3, 2]
    print("passed:", result == val, "expected", val, "got", result)

    root = TreeNode.from_list([1, None, 2, 3])
    result = inorder_traversal_iter(root)
    val = [1, 3, 2]
    print("passed:", result == val, "expected", val, "got", result)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    result = inorder_traversal_iter(root)
    val = [3, 2, 4, 1, 5]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
