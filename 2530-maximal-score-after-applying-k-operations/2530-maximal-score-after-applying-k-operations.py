import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # 최대 힙을 만들기 위해 nums의 값을 음수로 변환
        nums = [-num for num in nums]
        heapq.heapify(nums) # 최소 힙을 음수로 변환한 값들로 최대 힙처럼 사용
        
        total_score = 0
        
        # k번 반복하여 가장 큰 값을 선택하고 점수에 합산
        for _ in range(k):
            # 가장 큰 값 꺼내기(최대 힙이므로 음수를 꺼냄)
            max_value = -heapq.heappop(nums)
            
            # 점수에 더하기
            total_score += max_value
            
            # 3으로 나눈 후 올림 처리하여 다시 힙에 삽입
            new_value = math.ceil(max_value / 3)
            heapq.heappush(nums, -new_value)    # 음수로 변환하여 힙에 삽입
            
        return total_score  # 총 점수 반환