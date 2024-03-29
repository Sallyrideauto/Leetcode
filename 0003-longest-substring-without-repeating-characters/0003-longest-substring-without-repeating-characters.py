class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        char_to_index = {}
        for end, char in enumerate(s):
            if char in char_to_index and char_to_index[char] >= start:
                start = char_to_index[char] + 1
            char_to_index[char] = end
            max_length = max(max_length, end - start + 1)
        return max_length