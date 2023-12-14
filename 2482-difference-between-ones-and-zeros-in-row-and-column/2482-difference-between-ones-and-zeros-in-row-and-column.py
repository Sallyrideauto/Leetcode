class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ones_row = [0] * m
        zeros_row = [0] * m
        ones_col = [0] * n
        zeros_col = [0] * n
        
        # 각 행과 열의 1과 0의 개수를 세어 주기
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones_row[i] += 1
                    ones_col[j] += 1
                else:
                    zeros_row[i] += 1
                    zeros_col[j] += 1
                    
        # 차이 행렬 diff 생성
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]
                
        return diff