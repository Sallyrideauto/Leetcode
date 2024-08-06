from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_arr_sums = []
        
        # 모든 부분 배열의 합 계산
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                sub_arr_sums.append(current_sum)
                
        # 부분 배열의 합 정렬
        sub_arr_sums.sort()
        
        # 범위 내 합 계산
        result = sum(sub_arr_sums[left - 1 : right]) % (10 ** 9 + 7)
        
        return result