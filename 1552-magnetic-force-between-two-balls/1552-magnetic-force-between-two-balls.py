class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort() # 위치를 먼저 정렬
        
        def canPlaceBalls(distance):
            # 첫 번째 공은 항상 position[0]에 놓습니다.
            count, last_position = 1, position[0]
            
            # 다음 공을 거리 'distance' 이상으로 놓을 수 있는지 확인
            for i in range(1, len(position)):
                if position[i] - last_position >= distance:
                    count += 1
                    last_position = position[i]
                    if count == m:  # 필요한 만큼 공을 놓았다면
                        return True
                    
        # 이분 탐색 설정
        left, right = 1, position[-1] - position[0]
        best_dist = 0
            
        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                best_dist = mid # 유효한 거리이면 갱신
                left = mid + 1
            else:
                right = mid - 1
                    
        return best_dist