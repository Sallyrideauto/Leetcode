class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # suffixSum[i]는 i번째 위치부터 끝까지 돌의 총합을 저장
        suffixSum = [0] * n
        suffixSum[-1] = piles[-1]
        
        # suffixSum 계산
        for i in range(n - 2, -1, -1):
            suffixSum[i] = piles[i] + suffixSum[i + 1]
            
        # dp 배열 초기화(메모이제이션)
        dp = [[0] * (n + 1) for _ in range(n)]
        
        # 재귀 함수 정의
        def dpFunc(i, M):
            # 마지막 pile에 도달하면, 남은 모든 돌으르 가져갈 수 있음
            if i == n:
                return 0
            # 만약 남은 돌을 모두 가져갈 수 있다면
            if 2 * M >= n - i:
                return suffixSum[i]
            # 메모이제이션이 되어 있는 경우, 그 값을 반환
            if dp[i][M] > 0:
                return dp[i][M]
            
            # 최대 돌을 가져가기 위해 상대방이 가져갈 최소 돌을 고려
            min_stones = float('inf')
            for x in range(1, 2 * M + 1):
                min_stones = min(min_stones, dpFunc(i + x, max(M, x)))
                
            # 첫 번째 플레이어가 가져갈 수 있는 최대 돌
            dp[i][M] = suffixSum[i] - min_stones
            return dp[i][M]
        
        # 첫 번째 플레이어가 가져갈 수 있는 최대 돌 수 계산
        return dpFunc(0, 1)