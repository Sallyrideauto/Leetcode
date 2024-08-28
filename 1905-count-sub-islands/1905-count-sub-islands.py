class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(x, y):
            # 탐색 조건과 범위 확인
            if not (0 <= x < len(grid2) and 0 <= y < len(grid2[0]) and grid2[x][y] == 1):
                return True
            grid2[x][y] = 0  # 방문 처리
            isSub = grid1[x][y] == 1  # grid1에도 섬이 있는지 확인
            # 상하좌우 네 방향 탐색
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if not dfs(x + dx, y + dy):
                    isSub = False
            return isSub

        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:  # 아직 방문하지 않은 섬의 일부 시작점
                    if dfs(i, j):
                        count += 1
        return count