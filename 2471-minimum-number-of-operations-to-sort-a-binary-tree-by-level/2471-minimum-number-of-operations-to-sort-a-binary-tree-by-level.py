from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def level_order_traversal(root):
            """BFS를 이용하여 레벨별 노드 값 리스트 생성"""
            levels = []
            queue = deque([root])
            while queue:
                level = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node:
                        level.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                if level:
                    levels.append(level)
            return levels
        
        def min_swaps_to_sort(arr):
            """사이클 디컴포지션을 이용한 최소 스왑 계산"""
            sorted_arr = sorted(arr)
            index_map = {val: idx for idx, val in enumerate(sorted_arr)}
            visited = [False] * len(arr)
            swaps = 0
            
            for i in range(len(arr)):
                if visited[i] or index_map[arr[i]] == i:
                    continue
                cycle_size = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = index_map[arr[x]]
                    cycle_size += 1
                if cycle_size > 1:
                    swaps += cycle_size - 1
            return swaps
        
        # 1. 트리의 레벨별 노드 값 리스트 생성
        levels = level_order_traversal(root)
        
        # 2. 각 레벨에 대해 최소 스왑 횟수 계산
        total_swaps = sum(min_swaps_to_sort(level) for level in levels)
        
        return total_swaps
