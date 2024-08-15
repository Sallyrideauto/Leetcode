class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 5달러와 10달러 지폐의 개수를 저장할 변수
        five_dollars = 0
        ten_dollars = 0
        
        # 손님이 낸 지폐를 순서대로 처리
        for bill in bills:
            if bill == 5:
                five_dollars += 1   # 5달러를 받으면 저장
            elif bill == 10:
                if five_dollars > 0:
                    five_dollars -= 1   # 5달러 한 장으로 돈을 거슬러 줌
                    ten_dollars += 1    # 10달러를 받음
                else:
                    return False    # 잔돈을 거슬러 줄 수 없을 경우 False
            elif bill == 20:
                # 10달러 1장과 5달러 1장으로 잔돈을 주는 경우가 더 효율적
                if ten_dollars > 0 and five_dollars > 0:
                    ten_dollars -= 1
                    five_dollars -= 1
                elif five_dollars >= 3:
                    five_dollars -= 3   # 5달러 3장으로 돈을 거슬러 줌
                else:
                    return False    # 잔돈을 줄 수 없으면 False
                
        return True # 모든 고객에게 잔돈을 줄 수 있으면 True