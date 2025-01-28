from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            # 격자 범위를 벗어나거나, 물고기가 없거나, 이미 방문한 경우
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0

            # 현재 셀의 물고기 수 저장
            fish_count = grid[x][y]

            # 방문 처리
            grid[x][y] = 0

            # 상하좌우로 연결된 영역 탐색
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                fish_count += dfs(x + dx, y + dy)

            return fish_count

        # 격자의 크기
        m, n = len(grid), len(grid[0])
        max_fish = 0

        # 모든 셀을 탐색
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:  # 물고기가 있는 경우만 탐색
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish
