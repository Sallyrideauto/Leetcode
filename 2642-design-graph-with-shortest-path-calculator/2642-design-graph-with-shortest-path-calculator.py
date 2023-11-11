import heapq

class Graph:
    def __init__(self, n, edges):
        self.n = n  # 노드의 수
        # 그래프는 각 노드에 연결된 다른 노드와 비용을 저장하는 딕셔너리로 표현됩니다.
        self.graph = {i: [] for i in range(n)}
        # 주어진 엣지들로 그래프를 초기화합니다.
        for from_node, to_node, cost in edges:
            self.graph[from_node].append((to_node, cost))
    
    def addEdge(self, edge):
        # 새로운 엣지를 그래프에 추가합니다.
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))
    
    def shortestPath(self, node1, node2):
        # Dijkstra 알고리즘을 사용하여 최단 경로를 찾습니다.
        visited = [False] * self.n  # 방문한 노드를 기록하는 리스트
        min_heap = [(0, node1)]  # 우선순위 큐를 사용하여 가장 적은 비용의 노드부터 탐색합니다.
        
        while min_heap:
            cost, node = heapq.heappop(min_heap)  # 현재 노드와 비용
            if node == node2:
                return cost  # 목표 노드에 도달하면 비용을 반환
            if visited[node]:
                continue
            visited[node] = True
            # 연결된 모든 노드에 대하여
            for neighbour, edge_cost in self.graph[node]:
                if not visited[neighbour]:
                    heapq.heappush(min_heap, (cost + edge_cost, neighbour))
        
        return -1  # 경로가 없을 경우 -1을 반환