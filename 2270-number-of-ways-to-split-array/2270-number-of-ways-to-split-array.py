from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # 배열의 총합 계산

        # 왼쪽 부분 합 초기화 및 경우의 수 초기화
        left_sum = 0
        ways = 0

        # 배열 순회(마지막 요소는 나눌 수 없으므로 제외)
        for i in range(len(nums) - 1):
            left_sum += nums[i]  # 현재 요소를 왼쪽 부분 합에 추가
            right_sum = total_sum - left_sum  # 오른쪽 부분 합 계산

            # 조건을 만족하면 경우의 수 증가
            if left_sum >= right_sum:
                ways += 1

        return ways  # 결과 반환
