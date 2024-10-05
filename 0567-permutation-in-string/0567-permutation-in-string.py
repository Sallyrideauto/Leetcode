class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 기본 조건: s1이 s2보다 길면 바로 False 반환
        if len(s1) > len(s2):
            return False
        
        # 알파벳 26개에 대해 빈도 배열을 준비(a ~ z)
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # s1의 빈도 배열 계산
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        # 슬라이딩 윈도우 기법으로 부분 문자열 비교
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        # s2에서 윈도우를 이동시키며 비교
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:   # 모든 알파벳의 빈도 수가 같으면 True 반환
                return True
            
            # 오른쪽 끝 문자 추가
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] - 1 == s1_count[index]:
                matches -= 1
                
            # 왼쪽 끝 문자 제거
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] + 1 == s1_count[index]:
                matches -= 1
                
            l += 1
            
        return matches == 26    # 마지막 윈도우 체크