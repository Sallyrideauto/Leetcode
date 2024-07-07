# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        # 중요 지점을 저장할 리스트
        critical_points = []
        prev_val = head.val # 이전 노드 값 저장
        current = head.next
        index = 1   # 시작 인덱스
        
        # 연결 리스트 순회하면서 중요 지점 찾기
        while current.next:
            if (current.val > prev_val and current.val > current.next.val) or \
            (current.val < prev_val and current.val < current.next.val):
                critical_points.append(index)
            prev_val = current.val  # 이전 노드 값 업데이트
            current = current.next
            index += 1
            
        # 중요 지점이 두 개 미만이면 -1, -1 반환
        if len(critical_points) < 2:
            return [-1, -1]
        
        # 최소 거리와 최대 거리 계산
        min_distance = float('inf')
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])
        max_distance = critical_points[-1] - critical_points[0]
        
        return [min_distance, max_distance]