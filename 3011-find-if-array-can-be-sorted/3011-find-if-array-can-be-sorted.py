class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # 입력값을 즉시 수정하는 것을 방지
        # 입력 배열에 대한 복사
        values = nums.copy()
        
        for i in range(n):
            for j in range(n - i - 1):
                if values[j] <= values[j + 1]:
                    # 스왑 불필요
                    continue
                else:
                    if bin(values[j]).count("1") == bin(values[j + 1]).count("1"):
                        # 요소들 스왑
                        values[j], values[j + 1] = values[j + 1], values[j]
                    else:
                        return False
        return True