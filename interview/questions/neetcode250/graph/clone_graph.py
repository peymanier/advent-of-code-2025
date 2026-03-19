class Node:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def print(self):
        visited = []

        def dfs(node: Node):
            if node in visited:
                return

            visited.append(node)
            print(node)

            for nei in node.neighbors:
                dfs(nei)

        dfs(self)

    def __repr__(self):
        return f"{self.val=}, {[nei.val for nei in self.neighbors]}"


def clone_graph(start: Node) -> Node:
    old_to_new_map = {}

    def dfs(node: Node):
        if node in old_to_new_map:
            return old_to_new_map[node]

        cpy = Node(node.val)
        old_to_new_map[node] = cpy

        for nei in node.neighbors:
            cpy.neighbors.append(dfs(nei))

        return cpy

    return dfs(start)


# def clone_graph(start: Node) -> Node:
#     old_to_new_map = {}
#
#     def dfs_create_copies(node: Node):
#         if node in old_to_new_map:
#             return
#
#         old_to_new_map[node] = Node(node.val)
#
#         for nei in node.neighbors:
#             dfs_create_copies(nei)
#
#     visited = []
#
#     def dfs_connect_copies(node: Node):
#         if node in visited:
#             return
#
#         visited.append(node)
#
#         new_node = old_to_new_map[node]
#         for nei in node.neighbors:
#             new_node.add_neighbor(old_to_new_map[nei])
#             dfs_connect_copies(nei)
#
#     dfs_create_copies(start)
#     dfs_connect_copies(start)
#     return old_to_new_map[start]


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.add_neighbor(node2)
    node1.add_neighbor(node3)

    node2.add_neighbor(node1)
    node2.add_neighbor(node4)

    node3.add_neighbor(node4)
    node3.add_neighbor(node1)

    node4.add_neighbor(node2)
    node4.add_neighbor(node3)

    new_node1 = clone_graph(node1)
    new_node1.print()


if __name__ == "__main__":
    main()
