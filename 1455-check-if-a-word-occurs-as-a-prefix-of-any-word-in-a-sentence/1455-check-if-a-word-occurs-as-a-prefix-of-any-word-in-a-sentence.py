class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # 1. 문장을 단어로 나누기
        words = sentence.split()  # 공백을 기준으로 문장을 나눠서 단어 리스트로 만듦
        
        # 2. 단어 리스트를 순회하며 접두사 비교
        for i, word in enumerate(words):
            # 3. 현재 단어가 searchWord로 시작하는지 확인
            if word.startswith(searchWord):
                return i + 1  # 인덱스는 1부터 시작하므로 i에 1을 더해 반환
        
        # 4. 접두사로 일치하는 단어가 없을 경우 -1 반환
        return -1