from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # LIS 배열 계산
        LIS = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
                    
        # LDS 배열 계산
        LDS = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)
                    
        # 산 배열의 가능한 최대 길이 계산
        max_mountain_length = 0
        for i in range(1, n - 1):
            if LIS[i] > 1 and LDS[i] > 1:
                max_mountain_length = max(max_mountain_length, LIS[i] + LDS[i] - 1)
                
        # 최소 제거 횟수 계산
        return n - max_mountain_length