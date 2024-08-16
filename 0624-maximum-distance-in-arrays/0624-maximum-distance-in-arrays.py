class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # 초기값 설정
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        # 각 배열을 순회하면서 거리 계산
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            # 최대 거리 계산
            max_distance = max(max_distance, abs(current_max - min_val), abs(current_min - max_val))
            
            # min_val과 max_val 갱신
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)
            
        return max_distance