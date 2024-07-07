class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalDrank = numBottles # 처음에 마신 물병의 수
        emptyBottles = numBottles   # 빈 병의 수도 처음에는 마신 물병의 수와 같음
        
        while emptyBottles >= numExchange:
            newBottles = emptyBottles // numExchange    # 교환해서 얻을 수 있는 새 병의 수
            totalDrank += newBottles    # 총 마신 병의 수에 추가
            emptyBottles = emptyBottles % numExchange + newBottles  # 남은 빈 병의 수를 업데이트
            
        return totalDrank