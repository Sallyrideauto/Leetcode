class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
            
        for i in range(n):
            for j in range(n):
                index = 4 * (i * n + j)
                if grid[i][j] == '/':
                    union(index + 0, index + 3)
                    union(index + 1, index + 2)
                elif grid[i][j] == '\\':
                    union(index + 0, index + 1)
                    union(index + 2, index + 3)
                else:
                    union(index + 0, index + 1)
                    union(index + 1, index + 2)
                    union(index + 2, index + 3)
                    
                # Right cell and current cell union
                if j + 1 < n:
                    union(index + 1, 4 * (i * n + (j + 1)) + 3)
                    
                # Down cell and current cell union
                if i + 1 < n:
                    union(index + 2, 4 * ((i + 1) * n + j) + 0)
                    
        # Count distinct parents
        return sum(parent[i] == i for i in range(4 * n * n))