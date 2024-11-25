from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 초기 상태를 문자열로 변환
        start = ''.join(str(num) for row in board for num in row)
        target = '123450'  # 목표 상태

        # 각 인덱스에서 이동 가능한 인덱스를 미리 정의 (0부터 5까지)
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        # BFS를 위한 큐 초기화: (현재 상태, 이동 횟수)
        queue = deque([(start, 0)])
        visited = set([start])

        while queue:
            current, steps = queue.popleft()
            
            # 목표 상태에 도달하면 이동 횟수를 반환
            if current == target:
                return steps

            # 빈 칸(0)의 현재 위치를 찾음
            zero_index = current.index('0')
            
            # 현재 위치에서 이동 가능한 모든 위치로 상태 전이
            for move in moves[zero_index]:
                new_board = list(current)
                # 빈 칸과 인접한 칸을 교환
                new_board[zero_index], new_board[move] = new_board[move], new_board[zero_index]
                new_state = ''.join(new_board)
                
                # 새로운 상태가 방문한 적이 없다면 큐에 추가
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))

        # 목표 상태에 도달할 수 없는 경우 -1 반환
        return -1
