class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # num2의 1비트 개수 계산
        num2_ones = bin(num2).count('1')    # num2의 1비트 개수

        # num1의 비트 정보를 기반으로 최소화된 x 생성
        result = 0
        for i in range(31, -1, -1): # 높은 비트(31)부터 낮은 비트(0)까지 확인 
            if num2_ones > 0 and (num1 & (1 << i)): # num1의 비트가 1이면
                result |= (1 << i)  # 해당 비트를 x에 추가
                num2_ones -= 1  # 남은 1비트 개수 감소

        # 부족한 1비트를 낮은 비트에 추가
        for i in range(32):
            if num2_ones > 0 and not (result & (1 << i)):   # x의 해당 비트가 0이면
                result |= (1 << i)  # 해당 비트를 1로 설정
                num2_ones -= 1  # 남은 1비트 개수 감소

        return result