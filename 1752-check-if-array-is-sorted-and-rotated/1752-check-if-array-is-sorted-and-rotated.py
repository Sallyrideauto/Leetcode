from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0   # 감소(drop) 지점의 개수 세기

        # 배열의 각 인덱스 i에 대해, nums[i]와 다음 원소 (nums[(i+1) % n])를 비교
        for i in range(n):
            # 현재 원소가 다음 원소보다 큰 경우 감소 지점
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        # 회전된 정렬 배열이라면 감소 지점이 정확히 1개여야 함
        if count == 1:
            return True

        # 감소하는 지점이 없는 경우 count == 0
        # 이때 배열이 모두 동일하다면, 회전해도 결과가 동일하므로 회전된 배열로 간주
        if count == 0 and nums[0] == nums[-1]:
            return True

        # 그 외의 경우는 회전된 배열이 아님
        return False