from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right  = right

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        res = []
        stack = deque([root])
        while stack:
            level = []
            for _ in range(len(stack)):
                node = stack.popleft()
                level.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(level)
        return res
    
    def levelOrder_dfs(self, root):
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root,0)
        return res

