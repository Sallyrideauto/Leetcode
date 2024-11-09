class Solution:
    def minEnd(self, n: int, x: int) -> int:
        k = n - 1
        ans = x
        k_binary_index = 0
        i = 0
        while (1 << i) <= ans or (1 << k_binary_index) <= k:
            if (ans >> i) & 1 == 0:
                if (k >> k_binary_index) & 1 == 1:
                    ans |= 1 << i
                k_binary_index += 1
            i += 1
        return ans