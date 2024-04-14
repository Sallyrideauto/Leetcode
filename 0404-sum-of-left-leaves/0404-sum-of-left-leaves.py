# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, is_left: bool) -> int:
            if not node:
                return 0
            if not node.left and not node.right and is_left:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False) 
    
    def build_tree(nodes: List[int], index: int) -> TreeNode:
        if index >= len(nodes) or nodes[index] is None:
            return None
        root = TreeNode(nodes[index])
        root.left = build_tree(nodes, 2 * index + 1)
        root.right = build_tree(nodes, 2 * index + 2)
        return root