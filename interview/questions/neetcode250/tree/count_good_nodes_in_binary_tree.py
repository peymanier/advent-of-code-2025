from interview.structures.tree import TreeNode


def count_good_nodes(root):
    result = 0

    def dfs(node, maximum):
        if not node:
            return

        nonlocal result
        if node.val >= maximum:
            result += 1

        dfs(node.left, max(maximum, node.val))
        dfs(node.right, max(maximum, node.val))

        return

    dfs(root, float("-inf"))
    return result


def main():
    root = TreeNode.from_list([3, 1, 4, 3, None, 1, 5])
    result = count_good_nodes(root)
    val = 4
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
