class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # 배열이 비어 있는 경우 예외로 처리
        if not nums:
            return 0

        # 초기화: 첫 번째 원소부터 시작하면 길이는 1
        inc = 1 # 현재까지 이어진 증가 구간의 길이
        dec = 1 # 현재까지 이어진 감소 구간의 길이
        res = 1 # 전체 최대 길이

        # 두 번째 원소부터 배열 순회
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # 증가 구간 길이 1 증가, 감소 구간 초기화
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                # 감소 구간 길이 1 증가, 증가 구간 초기화
                dec += 1
                inc = 1
            else:
                # 같을 경우 둘 다 초기화
                inc, dec = 1, 1

            # 현재 최대 길이 갱신
            res = max(res, inc, dec)

        return res