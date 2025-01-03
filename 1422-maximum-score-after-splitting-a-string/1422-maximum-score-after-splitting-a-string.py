class Solution:
    def maxScore(self, s: str) -> int:
        # Step 1: 전체 '1'의 개수를 구함
        total_ones = sum(1 for char in s if char == '1')
        
        # Step 2: 초기화
        left_score = 0
        right_score = total_ones
        max_score = float('-inf')
        
        # Step 3: 문자열 순회 (마지막 인덱스는 제외 - 두 부분으로 나눠야 하므로)
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_score += 1
            else:
                right_score -= 1
            # 현재 점수 계산
            current_score = left_score + right_score
            max_score = max(max_score, current_score)
        
        return max_score