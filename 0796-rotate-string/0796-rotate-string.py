class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 길이가 다르면 바로 False 반환
        if len(s) != len(goal):
            return False
        
        # s를 두 번 이어붙인 문자열 생성
        double_s = s + s
        
        # goal이 double_s의 부분 문자열인지 확인
        return goal in double_s