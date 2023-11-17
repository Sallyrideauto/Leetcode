class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # 배열을 오름차순으로 정렬
        nums.sort()
        n = len(nums)
        max_pair_sum = 0
        
        # 배열의 양 끝에서부터 요소를 하나씩 짝지어 최대 쌍의 합 탐색
        for i in range(n // 2):
            # 현재 쌍의 합을 계산
            pair_sum = nums[i] + nums[n - 1 - i]
            # 최대 쌍의 합을 업데이트
            max_pair_sum = max(max_pair_sum, pair_sum)
            
        # 최소화된 최대 쌍의 합 반환
        return max_pair_sum