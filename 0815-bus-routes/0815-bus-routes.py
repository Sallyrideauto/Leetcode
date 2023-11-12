from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # 노선별 정류장을 매핑하기 위한 딕셔너리
        stops_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stops_to_routes[stop].add(i)
                
        # BFS를 위한 준비
        queue = deque([source])
        visited = set() # 방문한 정류장을 기록
        buses = 0   # 탑승한 버스의 수
        
        while queue:
            buses += 1
            length = len(queue)
            for _ in range(length):
                stop = queue.popleft()
                for route in stops_to_routes[stop]:
                    if route in visited:
                        continue
                    visited.add(route)
                    for next_stop in routes[route]:
                        if next_stop == target:
                            return buses
                        queue.append(next_stop)
                        
        return -1