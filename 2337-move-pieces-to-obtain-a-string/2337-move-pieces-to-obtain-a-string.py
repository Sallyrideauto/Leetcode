class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # L과 R 만 남긴 후 두 문자열이 동일한지 비교
        start_chars = [c for c in start if c != '_']
        target_chars = [c for c in target if c != '_']
        
        if start_chars != target_chars:
            return False
        
        # 각각의 L과 R의 위치를 비교하여 이동 가능 여부를 판단
        n = len(start)
        start_L_indices = [i for i in range(n) if start[i] == 'L']
        target_L_indices = [i for i in range(n) if target[i] == 'L']
        
        for i, j in zip(start_L_indices, target_L_indices):
            if i < j:  # L은 왼쪽으로만 이동 가능하므로, target의 위치가 start보다 왼쪽이어야 함
                return False

        start_R_indices = [i for i in range(n) if start[i] == 'R']
        target_R_indices = [i for i in range(n) if target[i] == 'R']
        
        for i, j in zip(start_R_indices, target_R_indices):
            if i > j:  # R은 오른쪽으로만 이동 가능하므로, target의 위치가 start보다 오른쪽이어야 함
                return False

        return True