import heapq
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # (값, 인덱스)의 튜플을 가지는 최소 힙 생성
        min_heap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(min_heap)
        
        # k번 연산 수행
        for _ in range(k):
            value, index = heapq.heappop(min_heap)  # 최소값 추출
            nums[index] = value * multiplier        # 값 업데이트
            heapq.heappush(min_heap, (nums[index], index))  # 힙에 다시 삽입
        
        return nums
