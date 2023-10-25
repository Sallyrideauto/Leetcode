class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # target 시간 이상 일한 직원의 수 계산
        count = 0
        
        # 각 직원의 시간을 반복하며 target 시간 이상 일했는지 확인
        for hour in hours:
            if hour >= target:
                count += 1
                
        return count