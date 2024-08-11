class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # 유틸리티 함수: 주어진 그리드에서 섬의 개수를 세는 함수
        def count_islands(grid):
            def dfs(x, y):
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                    return
                grid[x][y] = 0  # 방문한 섬을 0으로 마킹
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dfs(x + dx, y + dy)

            island_count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        island_count += 1
                        dfs(i, j)
            return island_count
        
        # 1. 먼저 초기 상태에서 섬의 개수를 세기
        if count_islands([row[:] for row in grid]) != 1:
            return 0
        
        # 2. 한 칸을 물로 바꿨을 때 섬이 분리되는지 확인
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands([row[:] for row in grid]) != 1:
                        return 1
                    grid[i][j] = 1
        
        # 3. 어떤 한 칸을 제거해도 섬이 분리되지 않는다면, 두 칸을 제거하면 무조건 분리됨
        return 2