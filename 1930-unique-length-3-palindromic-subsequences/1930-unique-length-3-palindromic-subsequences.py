class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # 1. 각 문자의 처음과 마지막 등장 위치를 저장할 딕셔너리
        first_pos = {}
        last_pos = {}
        
        # 2. 문자열을 순회하여 첫 등장과 마지막 등장 위치를 저장
        for i, char in enumerate(s):
            if char not in first_pos:
                first_pos[char] = i
            last_pos[char] = i
        
        # 3. 고유한 회문 부분 문자열의 개수를 계산
        unique_palindromes = 0
        for char in first_pos:
            start = first_pos[char]
            end = last_pos[char]
            if start < end:  # 최소 길이가 3이 되어야 함
                # 중간 문자 집합 계산
                middle_chars = set(s[start + 1:end])
                unique_palindromes += len(middle_chars)
        
        return unique_palindromes