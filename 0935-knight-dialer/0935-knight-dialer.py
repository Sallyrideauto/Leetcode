class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # 전화 패드 레이아웃을 정의합니다.
        phone_pad = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [-1, 0, -1]
        ]

        # 나이트의 가능한 움직임을 정의합니다.
        knight_moves = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]

        # 유효한 움직임인지 확인하는 함수입니다.
        def is_valid_move(x, y):
            return 0 <= x < 4 and 0 <= y < 3 and phone_pad[x][y] != -1

        # 다이나믹 프로그래밍 테이블을 초기화합니다.
        dp = [[[0] * 3 for _ in range(4)] for _ in range(n)]
        
        # 초기 상태 설정: 전화번호 길이가 1일 때 각 숫자에 나이트를 둘 수 있는 경우의 수는 1입니다.
        for i in range(4):
            for j in range(3):
                if phone_pad[i][j] != -1:
                    dp[0][i][j] = 1

        # 각 길이에 대해 전화번호를 구성하는 모든 가능한 경우의 수를 계산합니다.
        for i in range(1, n):
            for x in range(4):
                for y in range(3):
                    if phone_pad[x][y] != -1:
                        for move_x, move_y in knight_moves:
                            prev_x, prev_y = x + move_x, y + move_y
                            if is_valid_move(prev_x, prev_y):
                                dp[i][x][y] += dp[i - 1][prev_x][prev_y]
                                dp[i][x][y] %= MOD

        # 전화번호 길이 n에 대한 모든 가능한 숫자의 총합을 반환합니다.
        return sum(dp[n - 1][x][y] for x in range(4) for y in range(3)) % MOD