from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 노드 상태를 관리하는 배열(0: 미방문, 1: 방문 중, 2: 안전)
        color = [0] * len(graph)

        # DFS 함수 정의
        def dfs(node: int) -> bool:
            if color[node] > 0:
                # 이미 방문한 경우(1: 순환, 2: 안전)
                return color[node] == 2

            # 현재 노드를 방문 중으로 표시
            color[node] = 1
            for neighbor in graph[node]:
                # 순환이 발견된 경우
                if not dfs(neighbor):
                    return False

            # 순환이 없으면 안전한 노드로 표시
            color[node] = 2
            return True

        # 결과로 반환할 안전한 노드 리스트
        result = []
        for node in range(len(graph)):
            if dfs(node):
                result.append(node)

        return result