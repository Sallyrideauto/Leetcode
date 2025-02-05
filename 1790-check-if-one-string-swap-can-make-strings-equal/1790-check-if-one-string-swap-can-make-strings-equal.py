class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # 1. 두 문자열이 이미 같은 경우 (스왑 없이 동일)
        if s1 == s2:
            return True
        
        # 2. 두 문자열의 차이나는 인덱스를 저장할 리스트
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
                # 만약 차이가 2개를 초과하면, 한 번의 스왑으로 해결 불가능
                if len(diff) > 2:
                    return False
        
        # 3. diff의 길이가 2인 경우에만 스왑 후 두 문자열이 같아지는지 확인
        if len(diff) == 2:
            i, j = diff[0], diff[1]
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        # 4. 그 외의 경우는 한 번의 스왑으로 동일하게 만들 수 없음
        return False