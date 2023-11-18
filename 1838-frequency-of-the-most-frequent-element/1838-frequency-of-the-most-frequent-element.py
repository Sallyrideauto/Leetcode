'''
1. 입력된 배열 nums를 오름차순으로 정렬합니다.
2. 슬라이딩 윈도우를 사용하여 배열의 연속된 부분집합을 탐색합니다.
   윈도우의 왼쪽과 오른쪽 포인터를 left와 right로 정의합니다.
3. 오른쪽 포인터를 배열의 끝까지 이동시키면서, 각 단계에서 total 변수에 현재 윈도우 내의 모든 값들을 오른쪽 포인터에 위치한 값으로 만드는데 필요한 증가량을 더합니다.
4. 만약 total 값이 k를 초과하면, 윈도우의 크기를 줄입니다. 
   즉, 왼쪽 포인터를 오른쪽으로 이동시키고, total에서 윈도우 밖으로 이동된 값의 증가량을 뺍니다.
5. 각 단계마다 윈도우의 크기 (right - left + 1)는 해당 윈도우에서 도달할 수 있는 최대 빈도수를 나타냅니다.
   이 값을 max_freq 변수와 비교하여 업데이트합니다.
6. 최종적으로 max_freq 변수의 값, 즉 최대 가능 빈도수를 반환합니다.
'''

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 배열을 오름차순으로 정렬
        nums.sort()
        left = 0 # 슬라이딩 윈도우의 왼쪽 포인터
        total = 0 # 총합을 저장하는 변수
        max_freq = 1    # 최대 빈도수를 저장하는 변수
        
        # 오른쪽 포인터를 이동시키면서 슬라이딩 윈도우를 확장
        for right in range(1, len(nums)):
            # 오른쪽 포인터에 있는 요소를 현재 윈도우의 가장 큰 값으로 만드는 데 필요한 증분을 total에 더함
            total += (nums[right] - nums[right - 1]) * (right - left)
            
            # 만약 증분한 총합이 k를 초과하면, 윈도우의 크기를 줄임
            while total > k:
                total -= nums[right] - nums[left]
                left += 1
                
            # 최대 빈도수를 업데이트
            max_freq = max(max_freq, right - left + 1)
            
        return max_freq