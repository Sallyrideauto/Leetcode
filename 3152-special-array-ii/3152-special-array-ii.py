class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        d = list(range(n))
        
        for i in range(1, n):
            if nums[i] % 2 != nums[i - 1] % 2:
                d[i] = d[i - 1]
                
        result = []
        for fromi, toi in queries:
            result.append(d[toi] <= fromi)
            
        return result