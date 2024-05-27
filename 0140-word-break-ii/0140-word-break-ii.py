from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict) # 빠른 조회를 위한 집합
        memo = {}   # 메모이제이션을 위한 딕셔너리
        
        def backtrack(start: int) -> List[str]:
            if start in memo:   # 메모이제이션된 결과가 있다면 바로 반환
                return memo[start]
            if start == len(s): # 문자열의 끝에 도달했을 때
                return [""] # 성공적인 분할의 기저 조건
            
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sub in backtrack(end):
                        if sub:
                            sentences.append(word + " " + sub)
                        else:
                            sentences.append(word)
            memo[start] = sentences
            return sentences
        
        return backtrack(0)