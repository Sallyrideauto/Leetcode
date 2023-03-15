from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        prev_node = root
        
        while queue:
            curr_node = queue.popleft()
            
            if not curr_node:
                while queue:
                    if queue.popleft():
                        return False
                return True
            
            if prev_node is None and curr_node:
                return False
            
            queue.append(curr_node.left)
            queue.append(curr_node.right)
            
            prev_node = curr_node
            
        return True