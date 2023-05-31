class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [int(d) for d in str(num)]  # num의 각 자릿수 추출
        counts = [0] * 10  # 각 숫자의 등장 횟수 저장
        for digit in digits:
            counts[digit] += 1

        new1 = new2 = 0
        for i in range(1, 10):
            while counts[i] > 0:
                if new1 <= new2:
                    new1 = new1 * 10 + i
                else:
                    new2 = new2 * 10 + i
                counts[i] -= 1

        return new1 + new2