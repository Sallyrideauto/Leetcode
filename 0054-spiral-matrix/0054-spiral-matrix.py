from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 상단 행을 오른쪽으로 이동하며 추가
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1    # 상단 경계 한 칸 아래로 이동
            
            # 오른쪽 열을 아래로 이동하며 추가
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # 오른쪽 경계 한 칸 왼쪽으로 이동
            
            if top <= bottom:
                # 하단 행을 왼쪽으로 이동하며 추가
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1 # 하단 경계 한 칸 위로 이동
                
            if left <= right:
                # 왼쪽 열을 위로 이동하며 추가
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1   # 왼쪽 경계 한 칸 오른쪽으로 이동
                
        return result