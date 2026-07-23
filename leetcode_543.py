class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution(object):
    def diameterRecursiceDFS(self, root):
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left+right)
            return 1+ max(left, right)
        dfs(root)
        return res     

    def diameterIterativeDFS(self, root):
        stack = [root]
        mp = {None: (0,0)}
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(root.left)
            elif root.right and node.right not in mp:
                stack.append(root.right)
            else:
                node = stack.pop()
                leftheight, leftdiameter = mp[node.left]
                rightheight, rightdiameter = mp[node.right]
                mp[node] = (1 + max(leftheight,rightheight), max(leftheight+rightheight, leftdiameter, rightdiameter))
        return mp[root][1]
