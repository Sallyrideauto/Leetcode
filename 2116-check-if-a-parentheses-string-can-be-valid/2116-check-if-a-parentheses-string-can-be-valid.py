class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # 길이가 짝수여야만 유효한 VPS가 가능
        if len(s) % 2 != 0:
            return False

        # 왼쪽에서 오른쪽으로 확인
        open_balance = 0
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                open_balance += 1   # 열린 괄호로 간주
            else:
                open_balance -= 1   # 닫는 괄호로 감소
            if open_balance < 0:
                return False    # VPS 불가능

        # 오른쪽에서 왼쪽으로 확인
        close_balance = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                close_balance += 1  # 닫는 괄호로 간주
            else:
                close_balance -= 1  # 열린 괄호로 감소
            if close_balance < 0:
                return False    # VPS 불가능

        return True