class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1 # 초기 상태 설정
        
        for i in range(1, n + 1):
            # 오늘 출석
            for j in range(2):
                for k in range(3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD
                    
            # 오늘 지각
            for j in range(2):
                dp[i][j][1] = dp[i - 1][j][0] % MOD
                dp[i][j][2] = dp[i - 1][j][1] % MOD
                
            # 오늘 결석
            for k in range(3):
                dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD
                
        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD
                
        return result