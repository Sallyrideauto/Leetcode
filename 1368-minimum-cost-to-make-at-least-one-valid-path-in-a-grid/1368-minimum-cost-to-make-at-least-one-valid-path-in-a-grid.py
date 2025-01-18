from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [
            (0, 1),    # 오른쪽(1)
            (0, -1),    # 왼쪽(2)
            (1, 0),     # 아래쪽(3)
            (-1, 0)     # 위쪽(4)
        ]

        # 방문 기록을 위한 2D 배열
        visited = [[False] * n for _ in range(m)]

        # 덱 초기화 (비용, x, y)
        deque_queue = deque([(0, 0, 0)])

        while deque_queue:
            cost, x, y = deque_queue.popleft()

            # 도착점 도달 시 최소 비용 반환
            if (x, y) == (m - 1, n - 1):
                return cost

            # 이미 방문한 노드는 pass
            if visited[x][y]:
                continue
            visited[x][y] = True

            # 네 방향 탐색
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n: # 그리드 범위 체크
                    # 현재 방향과 이동 방향이 같은 경우 비용 0
                    if i + 1 == grid[x][y]:
                        deque_queue.appendleft((cost, nx, ny))  # 비용 0인 경우 앞쪽 삽입
                    else:
                        deque_queue.append((cost + 1, nx, ny))  # 비용 1인 경우 뒤쪽 삽입