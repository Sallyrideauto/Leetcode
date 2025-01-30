from collections import deque, defaultdict
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # 그래프 구성
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        
        def bfs(start):
            # BFS를 통한 그룹화 및 검증
            queue = deque([start])
            levels = [-1] * n
            levels[start] = 0
            max_level = 0
            while queue:
                node = queue.popleft()
                current_level = levels[node]
                for neighbor in graph[node]:
                    if levels[neighbor] == -1:
                        levels[neighbor] = current_level + 1
                        max_level = max(max_level, levels[neighbor])
                        queue.append(neighbor)
                    elif abs(levels[neighbor] - current_level) != 1:
                        return -1
            return max_level + 1
        
        visited = [False] * n
        total_groups = 0
        
        for i in range(n):
            if not visited[i]:
                # 연결 요소 탐색
                component_nodes = []
                queue = deque([i])
                visited[i] = True
                while queue:
                    node = queue.popleft()
                    component_nodes.append(node)
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # 각 연결 요소에 대해 BFS 수행
                max_groups = 0
                for node in component_nodes:
                    result = bfs(node)
                    if result == -1:
                        return -1
                    max_groups = max(max_groups, result)
                
                total_groups += max_groups
        
        return total_groups
