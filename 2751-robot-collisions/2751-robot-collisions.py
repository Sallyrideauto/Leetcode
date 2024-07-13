from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # 로봇을 위치 기준으로 정렬합니다.
        robots = sorted(zip(positions, healths, directions))
        
        stack = []
        
        for pos, health, dir in robots:
            if dir == 'R':
                stack.append((pos, health, dir))
            else:
                while stack and stack[-1][2] == 'R':
                    prev_pos, prev_health, prev_dir = stack[-1]
                    
                    if prev_health > health:
                        health = 0
                        stack[-1] = (prev_pos, prev_health - 1, prev_dir)
                    elif prev_health < health:
                        health -= 1
                        stack.pop()
                    else:
                        health = 0
                        stack.pop()
                        
                    if health == 0:
                        break
                        
                if health > 0:
                    stack.append((pos, health, dir))
        
        # 원래 입력 순서로 건강 상태를 반환하기 위해 딕셔너리를 사용합니다.
        pos_to_health = {pos: health for pos, health, dir in stack}
        
        # 원래 입력 순서대로 결과를 만듭니다. 딕셔너리에 없는 위치는 제거된 로봇이므로 포함하지 않습니다.
        result = [pos_to_health.get(pos, None) for pos in positions]
        
        # None 값을 제거합니다. (제거된 로봇의 위치)
        result = [health for health in result if health is not None]
        
        return result