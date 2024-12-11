from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Step 1: 각 요소의 범위 계산
        events = []
        for num in nums:
            events.append((num - k, 1))  # 시작 지점
            events.append((num + k + 1, -1))  # 끝 지점 (+1은 범위의 끝을 열림으로 처리)
        
        # Step 2: 이벤트 정렬
        events.sort()
        
        # Step 3: 슬라이딩 윈도우를 통한 최대 겹침 계산
        max_beauty = 0
        current_overlap = 0
        
        for _, value in events:
            current_overlap += value  # 겹치는 개수 갱신
            max_beauty = max(max_beauty, current_overlap)  # 최대 겹침 추적
        
        return max_beauty