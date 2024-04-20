class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    x, y = i, j
                    while x < len(land) and land[x][j] == 1:
                        x += 1
                    while y < len(land[0]) and land[i][y] == 1:
                        y += 1
                    res.append([i, j, x - 1, y - 1])
                    for a in range(i, x):
                        for b in range(j, y):
                            land[a][b] = 0
        return res