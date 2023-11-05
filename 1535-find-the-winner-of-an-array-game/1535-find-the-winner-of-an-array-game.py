class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current_winner = arr[0] # 현재 승자 초기화
        win_count = 0   # 현재 승자의 연속 승리 횟수 초기화
        
        # 리스트를 순회하며 게임 진행
        for i in range(1, len(arr)):
            if arr[i] > current_winner:
                # 새로운 요소가 이긴 경우, 승자와 승리 횟수를 갱신
                current_winner = arr[i]
                win_count = 1
            else:
                # 현재 승자가 또 이긴 경우, 승리 횟수만 증가
                win_count += 1
            
            # 연속 승리 횟수가 k에 도달하면 현재 승자 반환
            if win_count == k:
                break
            
        # 모든 라운드가 끝난 후 현재 승자 반환
        return current_winner