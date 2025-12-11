class Treenode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def insertintoBST(self, root, val):
        if not root:
            return Treenode(val)
        if val < root.val:
            root.left = self.insertintoBST(root.left, val)
        else:
            root.right = self.insertintoBST(root.right, val)
        return root


def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

sol = Solution()
root = None  # start with an empty tree

# Insert values one by one
for val in [5]:
    root = sol.insertintoBST(root, val)

# Print inorder (should be sorted)
print(inorder(root))   # Output: [2, 3, 4, 5, 6, 7, 8]
      