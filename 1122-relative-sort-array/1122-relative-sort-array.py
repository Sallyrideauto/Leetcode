from collections import Counter
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # arr1의 빈도 계산
        count = Counter(arr1)
        
        # 결과 배열 초기화
        result = []
        
        # arr2의 요소 처리
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]
            
        # 남아 있는 요소 처리
        for num in sorted(count.elements()):
            result.append(num)
            
        return result