class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = [[rStart, cStart]]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오른쪽, 아래, 왼쪽, 위
        x, y = rStart, cStart   # 초기 위치
        total_cells = rows * cols

        steps = 0   # 이동 거리
        while len(result) < total_cells:
            for i in range(4):
                if i % 2 == 0:  # 오른쪽이나 왼쪽으로 이동하는 경우
                    steps += 1
                for _ in range(steps):
                    x += directions[i][0]
                    y += directions[i][1]
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x, y])
                    if len(result) == total_cells:
                        return result
                    
        return result