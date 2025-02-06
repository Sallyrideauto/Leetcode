class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # 각 곱(prod)이 몇 번 나타나는지를 기록할 딕셔너리 초기화
        product_count = {}

        n = len(nums)
        # 모든 가능한 두 숫자 쌍에 대한 곱 계산(i < j)
        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                # 딕셔너리에 prod가 이미 존재하면 count 증가, 없으면 1로 초기화
                product_count[prod] = product_count.get(prod, 0) + 1

        # 결과값 초기화
        result = 0
        # 각 곱(prod)별로 튜플의 경우의 수를 계산
        for count in product_count.values():
            if count > 1:
                # count 개의 쌍 중 2개를 선택하는 경우의 수: C(count, 2)
                # 그리고 각 선택에서 8가지 튜플이 가능하므로 8을 곱함 
                result += 8 * (count * (count - 1) // 2)

        return result