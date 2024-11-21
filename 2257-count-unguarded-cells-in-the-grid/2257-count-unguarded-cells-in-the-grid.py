from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 그리드 초기화
        grid = [[0] * n for _ in range(m)]
        
        # 벽과 경비병 위치 설정
        for r, c in walls:
            grid[r][c] = -1 # 벽은 -1로 표시
        for r, c in guards:
            grid[r][c] = 1  # 경비병은 1로 표시
            
        # 경비병의 감시 영역 설정
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우 방향
        
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == -1 or grid[nr][nc] == 1:
                        break   # 벽이나 경비병을 만나면 중지
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 2    # 감시되는 셀을 2로 표시
                    nr += dr
                    nc += dc
                    
        # 보호되지 않은 셀 카운트
        unguarded_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguarded_count += 1
                    
        return unguarded_count