# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 더미 노드 생성
        current = dummy # 결과 리스트를 위한 현재 노드
        sum_ = 0    # 합계를 저장할 변수
        
        while head:
            if head.val == 0:
                if sum_ > 0:
                    current.next = ListNode(sum_)   # 새 노드 생성
                    current = current.next  # 현재 노드 업데이트
                    sum_ = 0    # 합계 초기화
            else:
                sum_ += head.val    # 값을 더하기
            head = head.next    # 다음 노드로 이동
                
        return dummy.next   # 더미 노드 다음 노드부터 결과 리스트 반환