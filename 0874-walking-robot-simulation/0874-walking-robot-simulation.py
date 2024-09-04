class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 방향 초기화: 북, 동, 남, 서
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = 0   # 시작 위치
        direction = 0   # 초기 방향(북쪽)
        max_distance = 0    # 최대 거리 제공
        # 장애물을 집합으로 변환
        obstacle_set = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -2:
                # 왼쪽 회전
                direction = (direction - 1) % 4
            elif command == -1:
                # 오른쪽 회전
                direction = (direction + 1) % 4
            else:
                for _ in range(command):
                    # 전진 시도
                    nx, ny = x + dx[direction], y + dy[direction]
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        max_distance = max(max_distance, x * x + y * y)
                    else:
                        break
                        
        return max_distance