from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 해시 테이블로 각 숫자의 빈도를 세어 저장합니다.
        count = defaultdict(int)
        for num in nums1:
            count[num] += 1
            
        # 결과를 저장할 리스트
        result = []
        
        # 두 번째 배열을 순회하면서 해시 테이블의 숫자와 매칭되는 경우
        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1 # 사용된 숫자는 빈도를 감소시킵니다.
                
        return result