class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # 첫 번째 간선
        edge1 = edges[0]
        # 두 번째 간선
        edge2 = edges[1]
        
        # 첫 번째 간선의 두 노드 중 하나가 두 번째 간선에도 등장하면 그 노드가 중심 노드
        if edge1[0] == edge2[0] or edge1[0] == edge2[1]:
            return edge1[0]
        else:
            return edge1[1]