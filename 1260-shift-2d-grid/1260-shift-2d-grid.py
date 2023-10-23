class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # convert the 2D grid into a 1D list
        flat_list = [grid[i][j] for i in range(m) for j in range(n)]
        
        # compute the effective shifts needed, as k could be larger than m * n
        k %= m * n
        
        # perform the shift on the 1D list
        flat_list = flat_list[-k:] + flat_list[:-k]
        
        # convert the 1D list back to a 2D grid
        result = [[flat_list[i * n + j] for j in range(n)] for i in range(m)]
        
        return result