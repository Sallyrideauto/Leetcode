class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        # 결과를 저장할 변수
        count = 0
        
        # 문자열에 있는 각 유니크한 문자에 대해서만 검사
        for char in set(s):
            # 현재 문자의 첫 등장 위치를 탐색
            first_index = s.find(char)
            # 현재 문자의 마지막 등장 위치 탐색
            last_index = s.rfind(char)
            
            # 처음과 마지막 등장 사이에 있는 유니크한 문자들의 수를 세어 회문 개수 세기
            if first_index != last_index:   # 두 인덱스가 다를 때만 가능한 회문 존재
                count += len(set(s[first_index + 1 : last_index]))
                
        return count