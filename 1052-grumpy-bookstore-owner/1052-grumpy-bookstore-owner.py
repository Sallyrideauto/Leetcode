class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_satisfied = 0
        max_extra_satisfied = 0
        current_extra_satisfied = 0
        
        # 기본 만족 고객 수 계산
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_satisfied += customers[i]
                
        # 첫 'minutes' 동안 추가 만족 고객 수 계산
        for i in range(minutes):
            if grumpy[i] == 1:
                current_extra_satisfied += customers[i]
                
        max_extra_satisfied = current_extra_satisfied
        
        # 슬라이딩 윈도우로 최대 추가 만족 고객 수 찾기
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                current_extra_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                current_extra_satisfied -= customers[i - minutes]
            max_extra_satisfied = max(max_extra_satisfied, current_extra_satisfied)
            
        return total_satisfied + max_extra_satisfied