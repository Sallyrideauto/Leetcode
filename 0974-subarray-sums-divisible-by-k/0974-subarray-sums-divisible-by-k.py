class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        remainder_count = {0: 1}    # 나머지가 0인 경우 최소 하나 존재
        
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod < 0: # 음수 나머지 대응
                mod += k
            if mod in remainder_count:
                count += remainder_count[mod]
            if mod in remainder_count:
                remainder_count[mod] += 1
            else:
                remainder_count[mod] = 1
                
        return count