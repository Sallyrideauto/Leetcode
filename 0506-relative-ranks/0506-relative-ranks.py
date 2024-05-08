class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # 점수에 대한 순위를 정렬하여 매핑할 해시 맵 생성
        sorted_scores = sorted(score, reverse = True)
        rank_map = {}
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)
                
        # 기존 점수 리스트를 매핑하여 순위 매핑
        return [rank_map[s] for s in score]