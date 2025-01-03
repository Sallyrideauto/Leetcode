from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # 모음 집합 정의
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # 각 단어가 모음으로 시작하고 끝나는지 여부를 계산
        is_vowel_word = [1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]
        
        # 프리픽스 합 계산
        prefix_sum = [0] * (len(words) + 1)
        for i in range(len(words)):
            prefix_sum[i + 1] = prefix_sum[i] + is_vowel_word[i]
        
        # 쿼리 처리
        result = []
        for l, r in queries:
            result.append(prefix_sum[r + 1] - prefix_sum[l])
        
        return result
