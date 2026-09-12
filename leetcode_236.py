class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def lowestCommonAncestor_recursion(self, root, p, q):
        if root is None:
            return None
        if root == p and root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        return right
    
    def lowestCommonAncestor_iterative(self, root, p, q):
        curr = root
        while curr:
            if p.val > curr and q.val > curr:
                curr = curr.right
            elif p.val < curr and p.val < curr:
                curr = curr.left
            else:
                return curr

                