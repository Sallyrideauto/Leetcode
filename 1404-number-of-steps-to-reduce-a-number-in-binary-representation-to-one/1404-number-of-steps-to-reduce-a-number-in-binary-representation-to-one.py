class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        while s != "1": # 1이 될 때까지 반복
            if s[-1] == '0':
                s = s[:-1]  # 짝수일 경우, 오른쪽 비트 삭제(2로 나누는 것과 동일)
            else:
                s = self.addOne(s)  # 홀수일 경우, 1 더하기
            steps += 1
        return steps
    
    def addOne(self, s: str) -> str:
        # 이진수 문자열에 1을 더하는 함수
        n = len(s)
        result = list(s)    # 문자열을 리스트로 변환하여 수정 가능하게 함
        carry = 1   # 초기 자리올림수
        for i in range(n - 1, -1, -1):
            if result[i] == '1' and carry == 1:
                result[i] = '0'
            elif carry == 1:
                result[i] = '1'
                carry = 0
                break
                
        if carry == 1:
            result.insert(0, '1')
            
        return ''.join(result)