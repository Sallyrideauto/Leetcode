class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0
        
        # 한 팀이 남을 때까지 경기를 진행
        while n > 1:
            # 현재 팀 수가 짝수일 경우
            if n % 2 == 0:
                matches = n // 2
                n = n // 2
            # 현재 팀 수가 홀수일 경우
            else:
                matches = (n - 1) // 2
                n = (n - 1) // 2 + 1
            # 경기 수를 총합에 더함
            total_matches += matches
            
        return total_matches