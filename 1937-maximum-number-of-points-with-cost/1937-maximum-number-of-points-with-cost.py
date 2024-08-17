class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        
        # 첫 번째 행의 값을 초기화
        prev_row = points[0]
        
        # 각 행을 순회하며 dp를 갱신
        for i in range(1, m):
            left_max = [0] * n
            right_max = [0] * n
            
            # 왼쪽에서 오른쪽으로 스위핑하여 left_max 계산
            left_max[0] = prev_row[0]
            for j in range(1, n):
                left_max[j] = max(left_max[j - 1] - 1, prev_row[j])
                
            # 오른쪽으로 왼쪽으로 스위핑하여 right_max 계산
            right_max[n - 1] = prev_row[n - 1]
            for j in range(n - 2, -1, -1):
                right_max[j] = max(right_max[j + 1] - 1, prev_row[j])
                
            # 현재 행의 최대 포인트 계산
            curr_row = [0] * n
            for j in range(n):
                curr_row[j] = points[i][j] + max(left_max[j], right_max[j])
                
            # 이전 행 갱신
            prev_row = curr_row
            
        # 마지막 행에서 최대값 반환
        return max(prev_row)