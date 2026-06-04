class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        old_graph = {}
        if node is None:
            return None
        def dfs(node):
            if node in old_graph:
                return old_graph[node]
            copy_graph = Node(node.val)
            old_graph[node] = copy_graph
            for nei in node.neighbors:
                copy_graph.neighbors.append(dfs(nei))
            return copy_graph
        return dfs(node )