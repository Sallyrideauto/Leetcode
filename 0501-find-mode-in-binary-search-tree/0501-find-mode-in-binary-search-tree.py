'''
이전 코드의 문제점은 중위 순회를 수행할 때, 이전 노드의 값과 현재 노드의 값이 다른 경우에만 카운트를 리셋하는 방식 때문에 발생합니다. 
이로 인해 트리의 끝에 도달할 때 현재 노드의 값이 이전 노드의 값과 동일한 경우, 빈도수가 최대 빈도와 동일하더라도 모드 목록에 추가되지 않습니다.

이 문제를 해결하기 위해서는 중위 순회가 끝난 후에 현재 노드의 빈도수를 최대 빈도와 비교하여 모드 목록을 갱신해야 합니다.
'''


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # 중위 순회를 수행하는 함수
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # 현재 노드의 값을 처리
            if self.prev == node.val:
                self.count += 1
            else:
                if self.count == self.max_count:
                    self.modes.append(self.prev)
                elif self.count > self.max_count:
                    self.max_count = self.count
                    self.modes = [self.prev]
                self.count = 1
            self.prev = node.val
            
            inorder(node.right)
            
        self.prev = None
        self.count = 0
        self.max_count = 0
        self.modes = []
        
        inorder(root)
        
        # 마지막 노드의 빈도수를 확인하고 모드 목록을 갱신
        if self.count == self.max_count:
            self.modes.append(self.prev)
        elif self.count > self.max_count:
            self.modes = [self.prev]
        
        return self.modes