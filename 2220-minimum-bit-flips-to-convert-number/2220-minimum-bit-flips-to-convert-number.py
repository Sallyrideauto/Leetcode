class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # start와 goal 사이의 XOR 연산 수행
        xored = start ^ goal
        
        # XOR 결과에서 1의 개수를 세어 반환
        return bin(xored).count('1')