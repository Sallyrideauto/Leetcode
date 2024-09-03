class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # 문자를 숫자로 변환
        transformed = ""
        for char in s:
            transformed += str(ord(char) - ord('a') + 1)
            
        # k번 반복하여 자릿수 합 계산
        for _ in range(k):
            sum_of_digits = sum(int(digit) for digit in transformed)
            transformed = str(sum_of_digits)
            
        return int(transformed)