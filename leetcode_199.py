from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView_bfs(self, root):
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            last_node = None
            for _ in range(len(queue)):
                node = queue.popleft()
                last_node = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return res.append(last_node.val)
        return res

    def rightSideView_dfs_recursion(self, root):
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root, 0)
        return res