from collections import defaultdict
from typing import List # 타입 힌트용으로 사용

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # 트리 생성
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
            
        # 각 노드에 대한 서브트리의 크기 및 거리의 합을 저장할 리스트
        subtree_size = [0] * n
        subtree_sum = [0] * n
        result = [0] * n
        
        # 루트 노드에서 시작하여 서브트리의 크기와 거리의 합을 계산하는 첫 번째 DFS
        def dfs1(node, parent):
            subtree_size[node] = 1 # 각 노드가 최소 1 크기를 가짐
            for child in tree[node]:
                if child == parent:
                    continue
                dfs1(child, node)
                subtree_size[node] += subtree_size[child]
                subtree_sum[node] += subtree_sum[child] + subtree_size[child]
                
        # 결과를 계산하는 두 번째 DFS
        def dfs2(node, parent):
            # 자식 노드의 거리의 합은 부모 노드의 거리의 합을 이용해 계산
            for child in tree[node]:
                if child == parent:
                    continue
                # 부모 노드로부터의 이동을 고려하여 자식 노드의 거리의 합을 계산
                result[child] = result[node] + (n - subtree_size[child]) - subtree_size[child]
                dfs2(child, node)
                
        # 루트 노드에서 첫 번째 DFS 시작
        dfs1(0, -1)
        # 루트 노드에서 거리의 합을 초기화
        result[0] = subtree_sum[0]
        # 두 번째 DFS를 통해 각 노드의 거리의 합을 계산
        dfs2(0, -1)
        
        return result