class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        
        if n == 0:
            return 0
        
        # dp 배열 초기화
        dp = [[0] * n for _ in range(n)]
        
        # 길이가 1인 경우 초기화
        for i in range(n):
            dp[i][i] = 1
            
        # 길이가 2 이상인 경우
        for length in range(2, n + 1):  # 부분 문자열의 길이
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = 1 + dp[i + 1][j] # 기본 경우
                
                # 중복 인쇄 최소화 조건 검사
                for k in range(i, j):
                    temp = dp[i][k] + dp[k + 1][j]
                    if s[k] == s[j]:
                        temp -= 1
                    dp[i][j] = min(dp[i][j], temp)
                    
        return dp[0][n - 1]