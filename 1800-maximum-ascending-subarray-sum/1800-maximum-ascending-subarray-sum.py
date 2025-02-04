class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # 첫 번째 원소로 current_sum과 max_sum 초기화
        current_sum = nums[0]
        max_sum = current_sum
        
        # 배열의 두 번째 원소부터 순회
        for i in range(1, len(nums)):
            # 이전 원소보다 현재 원소가 크다면 오름차순이므로 누적합에 더함
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                # 오름차순이 깨졌으므로 max_sum 갱신 후 current_sum을 현재 원소로 초기화
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        
        # 마지막 누적합과 max_sum 비교 후 최종 결과 반환
        max_sum = max(max_sum, current_sum)
        return max_sum
