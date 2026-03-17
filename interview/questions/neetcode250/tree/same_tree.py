from interview.structures.tree import TreeNode


def is_same_tree(r1, r2) -> bool:
    if not r1 and not r2:
        return True

    if not r1 or not r2:
        return False

    if r1.val != r2.val:
        return False

    return is_same_tree(r1.left, r2.left) and is_same_tree(r1.right, r2.right)


def main():
    tree = [1, 2, 3]
    root1 = TreeNode.from_list(tree)
    root2 = TreeNode.from_list(tree)
    result = is_same_tree(root1, root2)
    val = True
    print("passed:", result == val, "expected", val, "got", result)

    root1 = TreeNode.from_list([1, 2, 3])
    root2 = TreeNode.from_list([1, 2, 3, 4])
    result = is_same_tree(root1, root2)
    val = False
    print("passed:", result == val, "expected", val, "got", result)

    root1 = TreeNode.from_list([1, 2, 3])
    root2 = TreeNode.from_list([1, 2, 4])
    result = is_same_tree(root1, root2)
    val = False
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
