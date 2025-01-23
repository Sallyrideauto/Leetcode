from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # 높이 맵 초기화
        rows, cols = len(isWater), len(isWater[0])
        heightMap = [[-1 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        
        # 물 칸을 큐에 추가하고 높이를 0으로 설정
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    heightMap[i][j] = 0
        
        # BFS 방향 벡터 (상, 하, 좌, 우)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # BFS 수행
        while queue:
            x, y = queue.popleft()
            currentHeight = heightMap[x][y]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # 범위 내에 있고, 아직 방문하지 않은 칸인 경우
                if 0 <= nx < rows and 0 <= ny < cols and heightMap[nx][ny] == -1:
                    heightMap[nx][ny] = currentHeight + 1
                    queue.append((nx, ny))
        
        return heightMap