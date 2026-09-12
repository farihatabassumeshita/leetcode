class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree_recursion(self, root, subRoot):
        if subRoot is None:
            return True
        if root is None:
            return False
        elif self.isSubtree_recursion(root, subRoot):
            return True
        return (
            self.isSubtree_recursion(root.left, subRoot) or
            self.isSubtree_recursion(root.right, subRoot)
        )