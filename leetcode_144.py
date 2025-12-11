class Solution(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorderTraversal(self, root):
        result = []

        def bst(node):
            if not node:
                return
            result.append(node.val)
            bst(node.left)
            bst(node.right)

        bst(root)
        return result

sol = Solution()
root = Solution(1)
root.left = Solution(None)
root.right = Solution(2)
root.right.left = Solution(3)

print(sol.preorderTraversal(root))

