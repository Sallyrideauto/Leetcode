class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1    # 현재까지 만들 수 없는 가장 작은 수
        added = 0   # 추가된 수의 개수
        i = 0   # nums의 현재 인덱스
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
                
        return added