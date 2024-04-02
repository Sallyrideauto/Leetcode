class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s_arr = s.split()
        last_word = s_arr[-1]
        return len(last_word)