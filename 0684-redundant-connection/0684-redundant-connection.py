from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 노드의 부모를 저장하는 딕셔너리
        parent = {}
        
        # Find 연산: 경로 압축 기법 사용
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # 경로 압축
            return parent[node]

        # Union 연산: 두 노드를 하나의 집합으로 합침
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return False  # 두 노드가 이미 같은 집합에 있다면 사이클 발생
            parent[root2] = root1  # 집합 병합
            return True

        # 모든 간선에 대해 Union-Find 수행
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            
            if not union(u, v):  # 사이클이 발생하는 간선을 찾으면 반환
                return [u, v]

        return []
