class Treenode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val =val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        result = []

        def bst(node, level):
            if not node:
                return 
            if len(result) == level:
                result.append([])
            
            result[level].append(node.val)
            bst(node.left, level+1)
            bst(node.right, level+1)
        bst(root, 0)       
        return result