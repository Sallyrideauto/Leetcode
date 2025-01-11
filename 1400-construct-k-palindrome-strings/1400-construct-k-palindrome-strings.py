from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # 문자열의 길이가 k보다 작으면 k개의 회문을 만들 수 없음
        if len(s) < k:
            return False

        # 각 문자의 빈도 계산
        char_count = Counter(s)

        # 홀수 빈도를 가지는 문자 수 계산
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

        # 홀수 빈도 문자 수가 k보다 많으면 k개의 회문을 만들 수 없음
        if odd_count > k:
            return False

        # 조건을 만족하면 k개의 회문 구성 가능
        return True