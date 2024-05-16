from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # 첫 번째 열이 1이 되도록 모든 행 뒤집기
        for row in grid:
            if row[0] == 0:
                for j in range(len(row)):
                    row[j] ^= 1 # XOR 연산으로 0을 1로, 1을 0으로 뒤집기
                    
        # 각 열을 살펴보며 1의 개수 최대화
        rows, cols = len(grid), len(grid[0])
        for j in range(1, cols):
            num_ones = sum(grid[i][j] for i in range(rows))
            if num_ones < rows / 2:
                for i in range(rows):
                    grid[i][j] ^= 1 # XOR 연산으로 해당 열 뒤집기
                    
        # 최종 점수 계산
        score = 0
        for row in grid:
            row_value = 0
            for j in range(cols):
                row_value = row_value * 2 + row[j]  # 이진수로 간주하여 합 계산
            score += row_value
            
        return score