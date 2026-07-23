class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def balancedTree_RecursiveDFS(self, root):
        def dfs(root):
            if not root:
                return True
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                return False
            return  1 + max(left,right)
        dfs(root)
        return True
    
    def isbalanced_IterativeDFS(self, root):
        stack = [root]
        mp = {None : 0}
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftheight = mp[node.left]
                rightheight = mp[node.right]

                if abs(leftheight - rightheight) > 1:
                    return False
                mp[node] = 1 + max(leftheight,rightheight)
        return True
        
