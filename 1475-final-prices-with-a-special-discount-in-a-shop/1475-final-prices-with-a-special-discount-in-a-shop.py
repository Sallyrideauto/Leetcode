from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []  # 스택 초기화
        for i in range(len(prices)):
            # 스택 상단 값과 현재 값을 비교
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()  # 스택에서 인덱스 꺼내기
                prices[idx] -= prices[i]  # 할인 적용
            stack.append(i)  # 현재 인덱스를 스택에 추가
        return prices
