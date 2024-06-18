from typing import List
from bisect import bisect_right

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 일을 난이도에 따라 정렬하되, 동일 난이도일 경우 최대 수익 순으로 정렬
        jobs = sorted(zip(difficulty, profit), key=lambda x: (x[0], -x[1]))
        
        # 최대 수익 메모이제이션
        max_profit = 0
        new_jobs = []
        for d, p in jobs:
            max_profit = max(max_profit, p)
            new_jobs.append((d, max_profit))
            
        total_profit = 0
        
        # 작업자 능력에 따라 수익 계산
        for ability in worker:
            # 이분 탐색으로 해당 능력치 이하의 최대 수익 탐색
            index = bisect_right(new_jobs, (ability, float('inf'))) - 1
            if index >= 0:
                total_profit += new_jobs[index][1]
                
        return total_profit