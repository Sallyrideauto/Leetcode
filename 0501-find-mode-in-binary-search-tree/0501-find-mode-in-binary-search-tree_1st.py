'''
이 문제는 주어진 이진 탐색 트리에서 가장 빈도가 높은 요소(모드)를 찾는 문제입니다.

문제를 해결하기 위한 주요 아이디어는 BST의 중위 순회(inorder traversal)를 이용하는 것입니다. 
BST의 중위 순회는 정렬된 순서로 요소를 반환하기 때문에, 중위 순회를 수행하면서 연속된 중복 요소의 개수를 세고, 최대 빈도를 갱신하며 모드를 찾을 수 있습니다.

이론적 배경:
이 문제는 이진 탐색 트리의 특성과 트리 순회의 개념을 활용합니다. 
BST의 중위 순회는 트리의 요소를 정렬된 순서로 반환하므로, 이 특성을 활용하여 문제를 해결할 수 있습니다.

이 코드는 BST의 중위 순회를 사용하여 각 노드의 값을 순서대로 방문하면서 연속된 중복 요소의 개수를 세고, 
이 개수가 현재까지 발견한 최대 빈도보다 크다면 최대 빈도와 모드를 갱신합니다. 
중위 순회를 완료하면 모든 노드를 방문했으므로, 가장 빈도가 높은 요소(모드)를 찾을 수 있습니다.
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
                self.count += 1
            if self.count == self.max_count:
                self.modes.append(node.val)
            elif self.count > self.max_count:
                self.max_count = self.count
                self.modes = [node.val]
                
            self.prev = node.val
            inorder(node.right)
            
        self.prev = None
        self.count = 0
        self.max_count = 0
        self.modes = []
        
        inorder(root)
        
        return self.modes
