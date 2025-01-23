from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # 행과 열의 서버 개수 계산
        row_counts = [0] * len(grid)    # 각 행의 서버 개수
        col_counts = [0] * len(grid[0]) # 각 열의 서버 개수

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1

        # 통신 가능한 서버 개수 계산
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    count += 1

        return count