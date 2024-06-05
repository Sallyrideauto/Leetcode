from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # 첫 번째 문자열의 빈도수 계산
        common_count = Counter(words[0])
        
        # 두 번째 문자열부터 차례로 비교하여 최소 빈도 계산
        for word in words[1:]:
            word_count = Counter(word)
            # 공통으로 등장하는 최소 빈도 계산
            for char in common_count:
                common_count[char] = min(common_count[char], word_count[char])
                
        # 결과 리스트 생성
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
            
        return result