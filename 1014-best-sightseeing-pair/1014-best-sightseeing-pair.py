from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0  # 최대 점수를 저장
        max_i = values[0]  # 초기 i에 대한 values[i] + i 값
        
        # 배열 순회
        for j in range(1, len(values)):
            # 현재 최대 점수를 갱신
            max_score = max(max_score, max_i + values[j] - j)
            
            # max_i를 갱신
            max_i = max(max_i, values[j] + j)
        
        return max_score
