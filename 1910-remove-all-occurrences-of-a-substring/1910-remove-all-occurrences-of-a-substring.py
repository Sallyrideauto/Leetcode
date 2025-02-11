class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)

        # 문자열 s를 한 글자씩 순회
        for ch in s:
            stack.append(ch)
            # 스택의 길이가 part의 길이보다 크거나 같으면, 스택의 마지막 part_length 글자와 part를 비교
            if len(stack) >= part_length and ''.join(stack[-part_length:]) == part:
                # 만약 같다면 스택에서 해당 부분 제거
                for _ in range(part_length):
                    stack.pop()

        # 스택에 남은 문자들을 연결하여 결과 문자열을 반환
        return ''.join(stack)