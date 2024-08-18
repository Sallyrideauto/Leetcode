class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 첫 번째 ugly number 는 1
        ugly_numbers = [0] * n
        ugly_numbers[0] = 1
        
        # 세 개의 포인터 i2, i3, i5
        i2 = i3 = i5 = 0
        
        # 각 포인터가 가리키는 값의 배수를 미리 계산
        next_2 = 2
        next_3 = 3
        next_5 = 5
        
        # 2번째부터 n번째까지의 ugly number 계산
        for i in range(1, n):
            # 가장 작은 값이 새로운 ugly number가 됨
            next_ugly = min(next_2, next_3, next_5)
            ugly_numbers[i] = next_ugly
            
            # 해당 값이 어떤 포인터에서 생성되었는지 확인하고 갱신
            if next_ugly == next_2:
                i2 += 1
                next_2 = ugly_numbers[i2] * 2
            if next_ugly == next_3:
                i3 += 1
                next_3 = ugly_numbers[i3] * 3
            if next_ugly == next_5:
                i5 += 1
                next_5 = ugly_numbers[i5] * 5
                
        # n번째 ugly number 반환
        return ugly_numbers[-1]