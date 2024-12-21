from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # 그래프 인접 리스트 생성
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 방문 체크 및 컴포넌트 카운트
        visited = [False] * n
        self.components = 0

        def dfs(node: int) -> int:
            visited[node] = True
            subtotal = values[node]

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    subtotal += dfs(neighbor)

            # 서브트리 값이 k로 나누어 떨어지면 컴포넌트로 분리
            if subtotal % k == 0:
                self.components += 1
                return 0  # 상위 노드로 전달할 값은 없음

            # 나머지를 상위 노드로 전달
            return subtotal % k

        # 루트 노드에서 DFS 시작
        dfs(0)

        return self.components
