class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:  # 배열 길이가 4 이하인 경우 모든 요소를 제거할 수 있으므로 차이는 0
            return 0
        
        nums.sort() # 배열을 정렬
        
        # 다양한 경우 중 최소 차이 구하기
        return min(
            nums[-1] - nums[3],     # 가장 작은 3개를 제거하는 경우
            nums[-4] - nums[0],     # 가장 큰 3개를 제거하는 경우
            nums[-2] - nums[2],     # 가장 작은 2개와 가장 큰 1개를 제거하는 경우
            nums[-3] - nums[1]      # 가장 작은 1개와 가장 큰 2개를 제거하는 경우
        )