class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y, island_id):
            stack = [(x, y)]
            area = 0
            while stack:
                i, j = stack.pop()
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                    grid[i][j] = island_id
                    area += 1
                    for di, dj in directions:
                        stack.append((i + di, j + dj))
            return area

        island_id = 2
        island_area = {}

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, island_id)
                    island_area[island_id] = area
                    island_id += 1

        max_area = max(island_area.values(), default = 0)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen.add(grid[ni][nj])
                    new_area = 1 + sum(island_area[id] for id in seen)
                    max_area = max(max_area, new_area)

        return max_area