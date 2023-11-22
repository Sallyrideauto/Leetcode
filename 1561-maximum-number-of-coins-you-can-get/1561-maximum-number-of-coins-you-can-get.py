class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # 동전 더미를 내림차순으로 정렬
        piles.sort(reverse = True)
        
        # 동전 선택 및 합산
        coins = 0
        n = len(piles) // 3
        for i in range(n):
            # Alice가 가장 많은 동전을 가진 더미를 선택하고, 내가 두 번째 더미를 선택
            coins += piles[2 * i + 1]
            
        return coins