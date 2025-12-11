class Treenode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        result = []
        def preorder(node, path):
            if not node:
                return
            if not node.left and not node.right:
                result.append(path + str(node.val))
            else:
                preorder(node.left, path + str(node.val) + "->")
                preorder(node.right, path + str(node.val) + "->")
        preorder(root, "")
        return result