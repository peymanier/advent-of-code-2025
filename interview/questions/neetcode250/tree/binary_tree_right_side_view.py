from interview.structures.tree import TreeNode


def right_side_view(root):
    result = []

    que = [root]
    while que:
        right_node = None
        for _ in range(len(que)):
            curr = que.pop(0)
            right_node = curr.val

            if curr.left:
                que.append(curr.left)

            if curr.right:
                que.append(curr.right)

        if right_node:
            result.append(right_node)

    return result


def main():
    root = TreeNode.from_list([1, 2, 3, None, 5, None, 4])
    result = right_side_view(root)
    val = [1, 3, 4]
    print("passed:", result == val, "expected", val, "got", result)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.right.right = TreeNode(4)
    result = right_side_view(root)
    val = [1, 3, 4, 7]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
