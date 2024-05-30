class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        xor = [0] * (n + 1)
        for i in range(n):
            xor[i + 1] = xor[i] ^ arr[i]
            
        count = 0
        for i in range(n):
            for k in range(i + 1, n + 1):
                if xor[i] == xor[k]:
                    count += (k - i - 1)
                    
        return count