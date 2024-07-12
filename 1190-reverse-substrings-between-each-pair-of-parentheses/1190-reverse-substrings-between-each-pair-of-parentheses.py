class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current_string = []
        
        for char in s:
            if char == '(':
                # 현재 문자열을 스택에 저장
                stack.append(current_string)
                # 새로운 문자열 시작
                current_string = []
            elif char == ')':
                # 현재 문자열을 뒤집음
                current_string.reverse()
                # 스택에서 이전 문자열을 꺼내서 뒤집은 문자열을 이어 붙임
                current_string = stack.pop() + current_string
            else:
                # 일반 문자는 현재 문자열에 추가
                current_string.append(char)
                
        # 리스트를 문자열로 변환하여 반환
        return ''.join(current_string)