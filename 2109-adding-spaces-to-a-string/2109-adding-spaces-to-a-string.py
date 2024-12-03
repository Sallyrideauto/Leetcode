class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # 결과를 저장할 리스트
        result = []
        # 시작 인덱스 초기화
        start = 0
        
        # spaces 리스트를 순회
        for space in spaces:
            # 현재 start부터 space 인덱스까지 부분 문자열을 결과에 추가
            result.append(s[start:space])
            # 공백 추가
            result.append(" ")
            # 시작 인덱스를 현재 space 다음으로 갱신
            start = space
        
        # 마지막으로 남은 부분 문자열을 결과에 추가
        result.append(s[start:])
        
        # 리스트를 문자열로 결합하여 반환
        return "".join(result)
