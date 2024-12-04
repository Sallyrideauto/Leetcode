class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # 만약 str2가 str1보다 길면 부분 수열을 만들 수 없음
        if len(str2) > len(str1):
            return False

        i, j = 0, 0
        # str1을 순회하며 str2의 문자를 찾는다
        while i < len(str1) and j < len(str2):
            # 현재 문자가 동일하거나, 순환 증가하여 일치할 수 있는 경우
            if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                j += 1
            i += 1

        # str2의 모든 문자를 찾았는지 확인
        return j == len(str2)