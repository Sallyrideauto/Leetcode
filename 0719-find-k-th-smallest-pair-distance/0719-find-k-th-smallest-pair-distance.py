class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort() # 배열 정렬
        
        def count_pairs_with_distance_less_than_or_equal(mid):
            # 투 포인터로 거리 mid 이하인 쌍의 개수 세기
            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1  # i < j인 쌍만 고려
            return count
        
        left, right = 0, nums[-1] - nums[0] # 이진 탐색의 범위 설정
        
        while left < right:
            mid = (left + right) // 2
            if count_pairs_with_distance_less_than_or_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
                
        return left # 최종 결과 반환