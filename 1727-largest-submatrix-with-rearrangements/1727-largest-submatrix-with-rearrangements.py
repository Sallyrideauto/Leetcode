class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # 각 열에 대해 연속된 1열의 높이 계산
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:    # 만약 현재 값이 1이면, 이전 행이 값을 더함
                    matrix[i][j] += matrix[i - 1][j]
                    
        # 각 행에 대해 정렬하여 가능한 가장 큰 사각형의 면적 탐색
        max_area = 0
        for i in range(m):
            # 현재 행을 내림차순으로 정렬
            row = sorted(matrix[i], reverse = True)
            for j in range(n):
                # 현재 위치에서 가능한 최대 사각형의 면적을 계산
                max_area = max(max_area, row[j] * (j + 1))
                
        return max_area