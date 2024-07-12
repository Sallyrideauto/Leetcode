class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substrings(s, first, second, score):
            stack = []
            current_score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    current_score += score
                else:
                    stack.append(char)
            return ''.join(stack), current_score
        
        # 먼저 더 높은 점수를 주는 부분 문자열을 제거
        if x > y:
            s, score1 = remove_substrings(s, 'a', 'b', x)
            _, score2 = remove_substrings(s, 'b', 'a', y)
        else:
            s, score1 = remove_substrings(s, 'b', 'a', y)
            _, score2 = remove_substrings(s, 'a', 'b', x)
            
        return score1 + score2