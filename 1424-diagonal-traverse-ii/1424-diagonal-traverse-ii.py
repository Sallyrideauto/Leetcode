class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # 결과를 저장할 리스트
        result = []
        # 각 대각선의 합의 값들을 key로, 해당 대각선에 있는 요소들을 value로 저장할 딕셔너리
        diagonals = {}
        
        # 이중 for loop를 통해 각 요소의 대각선 계산
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                # 대각선 값을 계산하여 해당 key의 리스트에 요소를 추가
                diagonals[i + j].append(nums[i][j])
                
        # 대각선의 합이 작은 순서대로 요소들을 결과 리스트에 저장
        for key in sorted(diagonals.keys()):
            # 대각선 상의 요소들을 뒤집에서 결과 리스트에 추가
            result.extend(reversed(diagonals[key]))
            
        return result