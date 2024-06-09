from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 초기화
        cumulative_sum = 0
        remainder_map = {0: -1}
        
        for i, num in enumerate(nums):
            cumulative_sum += num
            if k != 0:
                cumulative_sum %= k
            
            if cumulative_sum in remainder_map:
                if i - remainder_map[cumulative_sum] > 1:
                    return True
                
            else:
                remainder_map[cumulative_sum] = i
                
        return False