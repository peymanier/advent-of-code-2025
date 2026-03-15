from interview.structures.tree import TreeNode


def preorder_traversal(root):
    result = []

    def traverse(node):
        if not node:
            return

        result.append(node.val)
        traverse(node.left)
        traverse(node.right)
        return

    traverse(root)
    return result


def preorder_traversal_iter(root):
    result = []
    stack = []
    curr = root
    while curr or stack:
        if not curr:
            curr = stack.pop()

        result.append(curr.val)

        if curr.right:
            stack.append(curr.right)

        curr = curr.left

    return result


def main():
    root = TreeNode.from_list([1, None, 2, 3])
    result = preorder_traversal(root)
    val = [1, 2, 3]
    print("passed:", result == val, "expected", val, "got", result)

    root = TreeNode.from_list([1, None, 2, 3])
    result = preorder_traversal_iter(root)
    val = [1, 2, 3]
    print("passed:", result == val, "expected", val, "got", result)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    result = preorder_traversal(root)
    val = [1, 2, 3, 4, 5]
    print("passed:", result == val, "expected", val, "got", result)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    result = preorder_traversal_iter(root)
    val = [1, 2, 3, 4, 5]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
