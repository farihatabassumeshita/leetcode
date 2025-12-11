class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorderTraversal(self, root):
        result = []

        def bst(node):
            if not node:
                return
            bst(node.left)
            result.append(node.val)
            bst(node.right)
        bst(root)
        return result

sol = TreeNode()  
root = TreeNode(1)
root.left = TreeNode(None)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(sol.inorderTraversal(root))