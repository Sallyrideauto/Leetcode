# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # 중위 순회로 트리의 원소를 배열에 저장
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)
        
        # 배열을 이용해 균형 잡힌 BST를 재구성
        def build_balanced_tree(nodes):
            if not nodes:
                return None
            mid = len(nodes) // 2
            root = nodes[mid]
            root.left = build_balanced_tree(nodes[:mid])
            root.right = build_balanced_tree(nodes[mid + 1:])
            return root
        
        nodes = inorder_traversal(root)
        return build_balanced_tree(nodes)