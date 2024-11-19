from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        current_sum = 0 # 현재 윈도우의 합
        max_sum = 0 # 최대 합
        start = 0   # 윈도우 시작점
        seen = set()    # 윈도우 내 중복 확인용 집합
        
        for end in range(n):
            # 새 요소 추가
            while nums[end] in seen:
                # 중복 제거를 위해 윈도우 시작점 이동
                seen.remove(nums[start])
                current_sum -= nums[start]
                start += 1
                
            # 현재 요소 추가
            seen.add(nums[end])
            current_sum += nums[end]
            
            # 윈도우 크기가 k일 때 최대값 갱신
            if end - start + 1 == k:
                max_sum = max(max_sum, current_sum)
                # 윈도우 축소
                seen.remove(nums[start])
                current_sum -= nums[start]
                start += 1
                
        return max_sum