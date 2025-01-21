class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        # 각 행의 누적 합 계산
        top_prefix = [0] * (n + 1)
        bottom_prefix = [0] * (n + 1)

        for i in range(n):
            top_prefix[i + 1] = top_prefix[i] + grid[0][i]
            bottom_prefix[i + 1] = bottom_prefix[i] + grid[1][i]

        # 두 번째 로봇이 얻을 수 있는 최소 점수의 최대값 계산
        result = float('inf')
        for i in range(n):
            # 첫 번째 로봇이 (0, 0)에서 (0, i)까지 이동한 후, (1, i)에서 (1, n-1)까지 이동하는 경우
            top_remaining = top_prefix[n] - top_prefix[i + 1]
            bottom_remaining = bottom_prefix[i]
            second_robot_score = max(top_remaining, bottom_remaining)
            result = min(result, second_robot_score)

        return result