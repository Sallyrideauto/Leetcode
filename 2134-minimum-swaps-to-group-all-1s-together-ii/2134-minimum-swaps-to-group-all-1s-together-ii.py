from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # 배열에서 1의 총 개수 k를 계산
        total_ones = sum(nums)
        n = len(nums)
        
        # 초기 슬라이딩 윈도우 설정
        current_ones = sum(nums[:total_ones])
        
        # 슬라이딩 윈도우를 이동하며 최대 1의 개수 찾기
        max_ones_in_window = current_ones
        for i in range(1, n):
            # 윈도우가 원형 배열을 넘어서도록 조정
            current_ones += nums[(i + total_ones - 1) % n] - nums[i - 1]
            max_ones_in_window = max(max_ones_in_window, current_ones)
            
        # 최소 교환 횟수 계산
        min_swaps = total_ones - max_ones_in_window
        return min_swaps