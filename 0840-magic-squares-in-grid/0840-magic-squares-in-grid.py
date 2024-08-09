from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(x: int, y: int) -> bool:
            # 3x3 매직 스퀘어를 검사하기 위한 값 추출
            values = [grid[x + i][y + j] for i in range(3) for j in range(3)]
            
            # 1부터 9까지의 숫자가 있는지 확인
            if sorted(values) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
            
            # 행, 열, 대각선의 합 계산
            row_sum = [sum(values[i * 3:(i + 1) * 3]) for i in range(3)]
            col_sum = [sum(values[i::3]) for i in range(3)]
            diag1_sum = sum(values[0::4])
            diag2_sum = sum(values[2:8:2])
            
            # 모든 합이 동일해야 함
            if len(set(row_sum + col_sum + [diag1_sum, diag2_sum])) == 1 and row_sum[0] == 15:
                return True
            return False
        
        count = 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagicSquare(i, j):
                    count += 1
        
        return count