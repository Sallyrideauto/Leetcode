import heapq
import math
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # 최대 힙 생성 (음수 값 사용)
        max_heap = []
        for g in gifts:
            heapq.heappush(max_heap, -g)
        
        # k번 연산
        for _ in range(k):
            # 최대값 추출
            x = -heapq.heappop(max_heap)
            # 새 값 = floor(sqrt(x))
            new_val = math.isqrt(x)  # math.isqrt는 floor(sqrt(x))와 동일
            # 힙에 새 값 삽입
            heapq.heappush(max_heap, -new_val)
        
        # 남은 선물 합산
        total = 0
        while max_heap:
            total += (-heapq.heappop(max_heap))
        
        return total
