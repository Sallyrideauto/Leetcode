from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        
        # 왼쪽에서 오른쪽으로 스캔
        count = 0  # 현재까지 만난 공의 수
        operations = 0  # 현재까지의 작업 횟수
        for i in range(n):
            result[i] += operations
            count += int(boxes[i])  # 현재 상자에 공이 있으면 카운트 증가
            operations += count  # 공의 수만큼 다음 상자로 이동
            
        # 오른쪽에서 왼쪽으로 스캔
        count = 0
        operations = 0
        for i in range(n - 1, -1, -1):
            result[i] += operations
            count += int(boxes[i])
            operations += count
            
        return result