# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numsSet = set(nums) # nums를 해시 세트로 변환
        # 더미 노드 생성 및 초기화
        dummy = ListNode(0)
        dummy.next = head
        # 현재 노드를 더미 노드로 초기화
        current = dummy
        
        # 연결 리스트 순회
        while current.next:
            # 현재 노드의 다음 노드 값이 numsSet에 있는 경우, 다음 노드를 제거
            if current.next.val in numsSet:
                current.next = current.next.next
            else:
                # 그렇지 않으면 다음 노드로 이동
                current = current.next
                
        return dummy.next   # 수정된 연결 리스트의 헤드 반환