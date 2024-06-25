# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverse_inorder(node, acc_sum):
            if not node:
                return acc_sum  # 이 부분이 누적합을 반영
            
            # 오른쪽 자식 먼저 방문(값이 큰 쪽)
            acc_sum = reverse_inorder(node.right, acc_sum)
            
            # 현재 노드 처리
            node.val += acc_sum
            acc_sum = node.val  # 업데이트된 노드의 값을 누적합에 추가
            
            # 왼쪽 자식 방문(값이 작은 쪽)
            return reverse_inorder(node.left, acc_sum)
        
        reverse_inorder(root, 0)
        return root