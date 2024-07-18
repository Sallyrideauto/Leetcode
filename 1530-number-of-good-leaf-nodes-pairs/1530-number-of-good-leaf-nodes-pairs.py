# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # 좋은 쌍을 계산
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        self.result += 1
                        
            # 거리를 업데이트하여 부모 노드로 변환
            new_distances = []
            for ld in left_distances:
                if ld + 1 <= distance:
                    new_distances.append(ld + 1)
            for rd in right_distances:
                if rd + 1 <= distance:
                    new_distances.append(rd + 1)
                    
            return new_distances
        
        dfs(root)
        return self.result