from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # 각 비트 위치별로 1의 개수를 저장할 배열
        bit_count = [0] * 32
        
        # 각 후보 숫자에 대해 비트를 검사
        for candidate in candidates:
            for i in range(32):
                # i번째 비트가 1인 경우 해당 비트 위치의 카운트를 증가
                if candidate & (1 << i):
                    bit_count[i] += 1
                    
        # 최대 비트 조합을 반환(1이 가장 많이 등장한 비트 위치의 카운트)
        return max(bit_count)