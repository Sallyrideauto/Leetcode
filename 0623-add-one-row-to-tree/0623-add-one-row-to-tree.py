# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        self.dfs(root, val, depth, 1)
        return root
    
    def dfs(self, node, val, depth, curr_depth):
        if not node:
            return
        if curr_depth == depth - 1:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, None, node.right)
        self.dfs(node.left, val, depth, curr_depth + 1)
        self.dfs(node.right, val, depth, curr_depth + 1)
        
    # Time complexity : O(N)
    # Space complexity : O(H) where H is the height of the tree