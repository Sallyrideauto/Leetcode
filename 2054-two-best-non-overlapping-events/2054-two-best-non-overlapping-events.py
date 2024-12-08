from bisect import bisect_right
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # 1. 종료 시간을 기준으로 정렬
        events.sort(key=lambda x: x[1])
        
        # 2. 종료 시간과 최대 가치 배열 생성
        end_times = [e[1] for e in events]
        max_value = [0] * len(events)
        
        # 3. 현재까지의 최대 가치 기록
        max_so_far = 0
        for i in range(len(events)):
            max_so_far = max(max_so_far, events[i][2])
            max_value[i] = max_so_far
        
        # 4. 최대 합계 결과
        result = 0
        for i in range(len(events)):
            start, end, value = events[i]
            
            # 이진 탐색으로 겹치지 않는 이전 이벤트 찾기
            index = bisect_right(end_times, start - 1) - 1
            
            # 현재 이벤트 + 이전 최대 이벤트 가치 계산
            if index >= 0:
                result = max(result, value + max_value[index])
            else:
                result = max(result, value)
        
        return result
