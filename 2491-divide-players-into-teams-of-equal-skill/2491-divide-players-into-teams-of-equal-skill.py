from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()    # skill 배열을 정렬
        
        team_sum = skill[0] + skill[-1] # 첫 번째 팀의 능력치 합을 계산
        total_score = 0
        
        # 팀을 구성하고 각 팀의 능력치 합과 곱을 확인
        for i in range(len(skill) // 2):
            if skill[i] + skill[-i - 1] != team_sum:
                return -1
            total_score += skill[i] * skill[-i - 1]
            
        return total_score  # 결과 반환