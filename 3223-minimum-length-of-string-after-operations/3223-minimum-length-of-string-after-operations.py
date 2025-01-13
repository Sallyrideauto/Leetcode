from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        # 각 문자의 빈도 계산
        char_frequency_map = Counter(s)

        # 제거 가능한 문자 수 계산
        delete_count = 0
        for frequency in char_frequency_map.values():
            # 빈도가 홀수인 경우 하나를 제외하고 모두 제거
            if frequency % 2 == 1:
                delete_count += frequency - 1
            # 빈도가 짝수인 경우 두 개를 제외하고 모두 제거
            else:
                delete_count += frequency - 2

        # 최소 길이 계산
        return len(s) - delete_count