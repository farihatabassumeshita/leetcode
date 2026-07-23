class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree_recursive(self, p, q):
        if p and q is None:
            return True
        elif p or q is None:
            return False
        elif p.val != q.val:
            return False
        return(
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )
    
    def isSameTree_iterative(self, p, q):
        stack = [(p,q)]
        while stack:
            p_node, q_node = stack.pop()

            if p_node is None and q_node is None:
                continue
            elif p_node is None or q_node is None:
                return False
            elif p_node.val != q_node.val:
                return False

            stack.append((p_node.left, q_node.left))
            stack.append((p_node.right, q_node.right))
        return True
        
    

