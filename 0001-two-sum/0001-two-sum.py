from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        
        # change to dictionary
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        # key = target - 1st num
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]