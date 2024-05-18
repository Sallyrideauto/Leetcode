# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def postorder(node):
            if not node:
                return 0
            
            left_balance = postorder(node.left)
            right_balance = postorder(node.right)
            
            # 현재 노드에서의 총 이동 횟수 계산
            self.moves += abs(left_balance) + abs(right_balance)
            
            # 현재 노드에서의 balance 계산
            current_balance = node.val + left_balance + right_balance - 1
            
            return current_balance
        
        postorder(root)
        
        return self.moves