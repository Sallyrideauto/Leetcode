class Solution:
    def findComplement(self, num: int) -> int:
        # num의 이진수 길이를 계산하기 위해 log를 사용하거나 bit_length() 사용
        bit_length = num.bit_length()
        
        # num과 같은 길이의 모든 비트가 1인 숫자를 생성
        # ex. num이 5(101)인 경우, mask는 111(7)
        mask = (1 << bit_length) - 1
        
        # num과 mask를 XOR 연산하여 보수를 구함
        return num ^ mask