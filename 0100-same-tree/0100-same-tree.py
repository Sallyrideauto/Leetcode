# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 두 트리가 모두 빈 트리인 경우
        if not p and not q:
            return True
        # 두 트리 중 하나만 빈 트리인 경우
        if not p or not q:
            return False
        # 현재 노드의 값이 다른 경우
        if p.val != q.val:
            return False
        # 왼쪽 서브트리와 오른쪽 서브트리를 재귀적으로 비교
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)