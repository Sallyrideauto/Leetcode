'''
로직 설명:
1. 배열에서 val과 일치하지 않는 요소를 찾으면서 배열의 시작 부분부터 그 값을 다시 채워 나갑니다. 
이를 통해 공간 복잡도를 O(1)로 유지하면서 배열을 수정합니다.
2. 배열의 시작 부분에서 부터 val과 일치하지 않는 요소를 채워 나가다가 val과 일치하는 요소를 만나면 그 위치에 새로운 값을 넣을 수 있습니다.
3. 이 과정을 통해 배열의 처음부터 k번째 요소까지는 val이 아닌 다른 요소로 채워지게 됩니다.
4. 함수는 k 값을 반환합니다.
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 시작 위치를 나타내는 인덱스
        index = 0
        
        # nums의 각 요소를 순회하면서
        for num in nums:
            # val과 일치하지 않는 요소를 찾으면
            if num != val:
                # 현재 index 위치에 num 값을 저장하고
                nums[index] = num
                # index를 1 증가시킴
                index += 1
                
        # index는 val과 일치하지 않는 요소의 개수와 같음
        return index