# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack, output = [root], []
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return output[::-1] # 후위 순회는 루트가 마지막이므로 결과를 뒤집어 반환