from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDistribute(maxBalls: int) -> bool:
            # 특정 maxBalls 값으로 모든 가방을 만족시키는지 확인
            operations = 0
            for balls in nums:
                # 각 가방에 필요한 작업 수 계산
                operations += (balls - 1) // maxBalls
                if operations > maxOperations:
                    return False
            return True
        
        # 이진 탐색 초기화
        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            if canDistribute(mid):
                high = mid  # 가능한 경우 더 작은 값을 찾기 위해 범위 축소
            else:
                low = mid + 1  # 불가능한 경우 더 큰 값을 찾기 위해 범위 확장
        
        return low