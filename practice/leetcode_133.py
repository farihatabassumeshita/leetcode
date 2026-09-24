class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        old_graph = {}
        def dfs(node):
            if node in old_graph:
                return old_graph[node]
            copy = Node(node.val)
            old_graph[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None

sol = Solution()
print(sol.cloneGraph(adjList = [[2,4],[1,3],[2,4],[1,3]]))