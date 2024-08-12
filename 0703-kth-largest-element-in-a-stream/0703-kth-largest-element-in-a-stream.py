import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)    # nums를 최소 힙으로 변환
        # 힙의 크기를 k로 유지
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)    # 가장 작은 요소 제거

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)  # 새로운 값을 힙에 추가
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)    # 힙의 크기를 k로 유지하기 위해 가장 작은 요소 제거
        return self.min_heap[0] # k번째로 큰 요소 반환


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)