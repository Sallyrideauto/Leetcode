from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 결과를 담을 리스트
        results = []
        # 중복 조합을 피하기 위해 candidates를 정렬
        candidates.sort()
        
        def backtrack(start, path, target):
            if target == 0:
                # 목표값을 달성한 경우 결과 리스트에 현재의 경로(path)를 추가
                results.append(path)
                return
            if target < 0:
                # 목표값을 초과한 경우 더 이상 진행하지 않고 종료
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    # 중복된 조합을 방지하기 위해 같은 층에서 이전에 사용한 숫자를 건너뜀
                    continue
                # 재귀 호출로 다음 숫자를 선택
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])
        
        # 백트래킹 시작
        backtrack(0, [], target)
        return results