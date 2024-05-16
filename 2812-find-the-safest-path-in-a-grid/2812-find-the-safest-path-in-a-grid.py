from collections import deque
from heapq import heappop, heappush

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def bfs_from_thieves(grid):
            rows, cols = len(grid), len(grid[0])
            dist = [[float('inf')] * cols for _ in range(rows)]
            q = deque()
            
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1: # 도둑의 위치
                        q.append((r, c))
                        dist[r][c] = 0
                        
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == float('inf'):
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))
                        
            return dist
        
        def canAchieveSafety(safety, dist, grid):
            rows, cols = len(grid), len(grid[0])
            heap = [(-dist[0][0], 0, 0)]    # (negative safety, row, col)
            visited = set()
            visited.add((0, 0))
            
            while heap:
                curr_safety, r, c = heappop(heap)
                curr_safety = -curr_safety
                if r == rows - 1 and c == cols - 1: # 목적지 도착
                    return True
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and dist[nr][nc] >= safety:
                        visited.add((nr, nc))
                        heappush(heap, (-dist[nr][nc], nr, nc))
            return False
        
        dist = bfs_from_thieves(grid)
        left, right = 0, min(dist[0][0], dist[-1][-1])
        
        while left < right:
            mid = (left + right + 1) // 2
            if canAchieveSafety(mid, dist, grid):
                left = mid
            else:
                right = mid - 1
                
        return left