class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort() # 배열 정렬
        moves = 0   # 필요한 증가 횟수 초기화
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:  # 현재 원소가 이전 원소보다 작거나 같다면
                prev = nums[i]
                nums[i] = nums[i - 1] + 1   # 이전 원소보다 1 크게 설정
                moves += nums[i] - prev # 증가분을 총합에 추가
        return moves