# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0:   # False leaf node
            return False
        if root.val == 1:   # True leaf node
            return True
        if root.val == 2:   # OR operator
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        if root.val == 3:   # AND operator
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)