from interview.structures.tree import TreeNode


def postorder_traversal(root):
    result = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)
        return

    traverse(root)
    return result


def postorder_traversal_iter(root):
    result = []
    stack = [root]
    visited = [False]
    while stack:
        curr = stack.pop()
        is_visited = visited.pop()
        if not curr:
            continue

        if is_visited:
            result.append(curr.val)
            continue

        stack.append(curr)
        visited.append(True)

        stack.append(curr.right)
        visited.append(False)

        stack.append(curr.left)
        visited.append(False)

    return result


def main():
    root = TreeNode.from_list([1, None, 2, 3])
    result = postorder_traversal(root)
    val = [3, 2, 1]
    print("passed:", result == val, "expected", val, "got", result)

    root = TreeNode.from_list([1, None, 2, 3])
    result = postorder_traversal_iter(root)
    val = [3, 2, 1]
    print("passed:", result == val, "expected", val, "got", result)

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    result = postorder_traversal(root)
    val = [1, 2, 3, 4, 5]
    print("passed:", result == val, "expected", val, "got", result)

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    result = postorder_traversal_iter(root)
    val = [1, 2, 3, 4, 5]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
