import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # 최대 힙을 저장할 리스트
        max_heap = []

        # 각 클래스의 초기 delta 값을 계산하여 힙에 삽입
        for passed, total in classes:
            delta = (passed + 1) / (total + 1) - passed / total
            heapq.heappush(max_heap, (-delta, passed, total))
        
        # extraStudents 만큼 반복
        for _ in range(extraStudents):
            # delta가 가장 큰 클래스를 가져옴
            delta, passed, total = heapq.heappop(max_heap)
            # 해당 클래스에 학생 1명 추가
            passed += 1
            total += 1
            # 학생 추가 후 새로운 delta 값을 계산
            new_delta = (passed + 1) / (total + 1) - passed / total
            # 힙에 다시 삽입
            heapq.heappush(max_heap, (-new_delta, passed, total))
        
        # 최종 평균 통과율 계산
        total_average = 0
        for _, passed, total in max_heap:
            total_average += passed / total
        
        return total_average / len(classes)
