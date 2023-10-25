class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 만역 nums가 비어 있다면 0을 반환
        if not nums:
            return 0
        
        # i는 현재 고유한 값의 위치를 가리킴
        i = 0
        
        # j를 사용하여 nums 배열을 반복하며 중복 항목 탐색
        for j in range(1, len(nums)):
            # nums[j]가 nums[i]와 다르면, 중복이 아니므로 nums[i + 1]에 값을 할당하고 i를 증가시킴
                if nums[j] != nums[i]:
                    i += 1
                    nums[i] = nums[j]
                    
        # 고유한 값의 수인 i + 1을 반환
        return i + 1