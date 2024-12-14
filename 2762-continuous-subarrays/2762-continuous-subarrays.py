from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sorted_window = SortedList()  # 정렬된 윈도우
        left = 0
        count = 0  # 조건을 만족하는 서브어레이 개수
        
        for right in range(len(nums)):
            # 오른쪽 포인터의 요소를 윈도우에 추가
            sorted_window.add(nums[right])
            
            # 조건이 깨지면 왼쪽 포인터를 이동
            while sorted_window[-1] - sorted_window[0] > 2:  # max - min > 2
                sorted_window.remove(nums[left])
                left += 1
            
            # 조건을 만족하는 서브어레이 개수 계산
            count += (right - left + 1)
        
        return count