from interview.structures.tree import TreeNode

# def max_depth_binary_tree(root):
#     if not root:
#         return 0
#
#     return 1 + max(max_depth_binary_tree(root.left), max_depth_binary_tree(root.right))


# def max_depth_binary_tree(root):
#     que = [root]
#     result = 0
#     while que:
#         n = len(que)
#         for i in range(n):
#             curr = que.pop(0)
#
#             if curr.left:
#                 que.append(curr.left)
#
#             if curr.right:
#                 que.append(curr.right)
#
#         result += 1
#
#     return result


def max_depth_binary_tree(root):
    stack = [(root, 1)]
    result = 0
    while stack:
        curr, depth = stack.pop()
        result = max(result, depth)

        if curr.right:
            stack.append((curr.right, depth + 1))

        if curr.left:
            stack.append((curr.left, depth + 1))

    return result


def main():
    tree = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.from_list(tree)
    result = max_depth_binary_tree(root)
    val = 3
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
