class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (n + m)  # 전체 주사위 던지기 결과의 총합
        missing_sum = total_sum - sum(rolls)    # 누락된 주사위 던지기 결과의 총합
        
        if not n <= missing_sum <= 6 * n:
            # 누락된 결과의 총합이 n ~ 6n 사이여야 함
            return []   # 조건을 만족하지 않으면 빈 배열 반환
        
        quotient, remainder = divmod(missing_sum, n)
        result = [quotient] * n # 일단 모든 누락된 결과를 평균값으로 채움
        
        for i in range(remainder):
            # 나머지 값을 배열에 순차적으로 추가하여 종합적으로 맞춤
            result[i] += 1
            
        return result