from heapq import heappush, heappop
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Min-Heap 생성
        heap = []
        for i, num in enumerate(nums):
            heappush(heap, (num, i))  # (값, 인덱스) 형태로 삽입
        
        # 마킹 상태 저장 리스트
        marked = [False] * len(nums)
        score = 0

        # Min-Heap 처리
        while heap:
            value, idx = heappop(heap)
            # 이미 마킹된 요소는 건너뛴다
            if marked[idx]:
                continue

            # 현재 값을 점수에 추가
            score += value

            # 현재 요소와 양 옆 요소를 마킹
            marked[idx] = True
            if idx > 0:  # 왼쪽 요소가 존재하면
                marked[idx - 1] = True
            if idx < len(nums) - 1:  # 오른쪽 요소가 존재하면
                marked[idx + 1] = True

        return score
