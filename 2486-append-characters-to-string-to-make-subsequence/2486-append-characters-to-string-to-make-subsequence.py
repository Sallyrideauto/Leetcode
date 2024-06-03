class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # 두 포인터 초기화
        i, j = 0, 0
        
        # s와 t를 순회하며 부분 문자열 탐색
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
            
        # t의 나머지 문자의 수가 추가해야 할 문자 수
        return len(t) - j