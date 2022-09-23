class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 데크 자료형 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True