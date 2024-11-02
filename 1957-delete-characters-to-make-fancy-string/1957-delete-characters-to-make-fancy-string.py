class Solution:
    def makeFancyString(self, s: str) -> str:
        result = [] # 결과 문자열을 저장할 리스트
        
        for char in s:
            # 결과 리스트의 길이가 2 이상이고 마지막 두 문자가 현재 문자와 같은지 확인
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue    # 조건을 위반하므로 문자를 추가하지 않음
            
            result.append(char) # 조건을 만족하면 문자를 추가
            
        # 리스트를 문자열로 변환하여 반환
        return ''.join(result)