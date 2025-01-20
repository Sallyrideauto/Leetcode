from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # 1. 숫자의 위치를 저장하는 딕셔너리 생성
        pos = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                pos[mat[i][j]] = (i, j)

        # 2. 행과 열의 페인트 상태를 추적하기 위한 배열 초기화
        row_paint = [0] * len(mat)  # 각 행의 페인트 개수
        col_paint = [0] * len(mat[0])  # 각 열의 페인트 개수

        # 3. 페인트 진행
        for idx, number in enumerate(arr):
            if number in pos:
                # 페인트할 숫자의 위치 (row, col)
                row, col = pos[number]
                
                # 해당 위치의 행과 열 페인트 상태 업데이트
                row_paint[row] += 1
                col_paint[col] += 1

                # 4. 완전히 색칠된 행 또는 열인지 확인
                if row_paint[row] == len(mat[0]) or col_paint[col] == len(mat):
                    return idx

        return -1  # 모든 행과 열이 페인트되지 않은 경우