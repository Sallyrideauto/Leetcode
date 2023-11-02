'''
이 문제는 주어진 이진 트리에서 각 노드의 값이 그 노드의 서브트리 값의 평균과 같은 노드의 수를 찾는 문제입니다.

문제를 해결하기 위한 주요 아이디어는 재귀적으로 각 노드의 서브트리의 합과 노드의 수를 구하고, 이를 이용해 서브트리의 평균을 구하는 것입니다. 
평균은 합을 노드의 수로 나눈 값입니다. 만약 평균이 노드의 값과 같다면 카운터를 증가시킵니다.

이론적 배경:
이 문제는 재귀와 트리 순회의 개념을 활용합니다. 트리의 각 노드를 방문하면서 재귀적으로 그 노드의 서브트리의 합과 노드의 수를 구합니다.
'''

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # 재귀적으로 노드의 서브트리 합과 노드의 수를 구하는 함수
        def dfs(node):
            if not node:
                return (0, 0) # (합, 노드 수)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count
            
            # 노드의 값이 서브트리의 평균과 같다면 카운터 증가
            if total_sum // total_count == node.val:
                self.count += 1
            
            return (total_sum, total_count)
        
        self.count = 0
        dfs(root)

        return self.count