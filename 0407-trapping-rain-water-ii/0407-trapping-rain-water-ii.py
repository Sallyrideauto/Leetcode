from heapq import heappop, heappush
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        heap = []

        # Step 1: 경계 셀 초기화
        for r in range(rows):
            for c in [0, cols - 1]:
                heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        for c in range(cols):
            for r in [0, rows - 1]:
                heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True

        # Step 2: BFS 탐색
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        water_trapped = 0

        while heap:
            height, r, c = heappop(heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # 물이 고일 수 있는 높이 계산
                    water_trapped += max(0, height - heightMap[nr][nc])
                    # 이웃 셀의 높이를 업데이트 후 Min-Heap에 추가
                    heappush(heap, (max(height, heightMap[nr][nc]), nr, nc))

        return water_trapped