from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # words2의 문자 조건 계산
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char in word_count:
                max_freq[char] = max(max_freq[char], word_count[char])

        # words1에서 조건 만족 여부 확인
        result = []
        for word in words1:
            word_count = Counter(word)
            # 모든 문자가 조건을 만족하는지 확인
            if all(word_count[char] >= max_freq[char] for char in max_freq):
                result.append(word)

        return result