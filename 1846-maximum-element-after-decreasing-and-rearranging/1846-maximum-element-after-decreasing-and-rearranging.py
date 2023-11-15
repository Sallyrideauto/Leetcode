class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # 배열 오름차순 정렬
        arr.sort()
        
        # 첫 번째 요소를 1로 설정
        arr[0] = 1
        
        # 두 번째 요소부터 시작하여 배열 순회
        for i in range(1, len(arr)):
            # 현재 요소를 이전 요소의 값에 1을 더한 값과 비교하여 더 작은 값을 선택하여 값을 갱신
            # 이는 인접한 요소간의 절대 차이가 1 이하가 되도록 함
            arr[i] = min(arr[i], arr[i - 1] + 1)
            
        # 마지막 요소가 최대값이 되도록 조정된 배열에서 최대값을 반환
        return arr[-1]