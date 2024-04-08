class Solution:
    def checkValidString(self, s: str) -> bool:
        left, right = 0, 0
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '*':
                left += 1
            else:
                left -= 1
            if left < 0:
                return False
        
        if left == 0:
            return True
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or s[i] == '*':
                right += 1
            else:
                right -= 1
            if right < 0:
                return False
            
        return True