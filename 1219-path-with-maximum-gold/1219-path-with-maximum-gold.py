from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # DFS를 이용하여 최대 금을 찾는 함수
        def dfs(x: int, y: int) -> int:
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            original_value = grid[x][y]
            grid[x][y] = 0  # 현재 셀을 방문한 것으로 표시
            max_gold = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                max_gold = max(max_gold, dfs(x + dx, y + dy))
            grid[x][y] = original_value # 백트래킹: 셀 값을 원래대로 복구
            return max_gold + original_value
        
        max_gold_collected = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold_collected = max(max_gold_collected, dfs(i, j))
                    
        return max_gold_collected