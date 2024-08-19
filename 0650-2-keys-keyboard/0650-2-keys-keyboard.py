class Solution:
    def minSteps(self, n: int) -> int:
        # dp 배열 생성, dp[i]는 i개의 A를 만드는 최소 작업 횟수
        dp = [0] * (n + 1)
        
        # dp 채우기
        for i in range(2, n + 1):
            dp[i] = i   # 초기값으로 최대 작업 횟수는 i(한 번씩 모두 붙여넣는 방식)
            
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))
                    
        return dp[n]