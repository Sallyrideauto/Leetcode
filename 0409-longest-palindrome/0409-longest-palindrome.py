class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Step 1: 문자의 빈도 계산
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        # Step 2: 회문 길이 계산
        length = 0
        has_odd = False
        for char in count:
            if count[char] % 2 == 0:
                length += count[char]
            else:
                length += count[char] - 1
                has_odd = True
        
        # Step 3: 중앙에 하나의 문자를 배치할 수 있는지 확인
        if has_odd:
            length += 1
            
        return length