class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # 문장을 단어 단위로 분할
        words = sentence.split()
        
        # 각 단어의 마지막 문자와 다음 단어의 첫 문자를 비교
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False
            
        # 마지막 단어와 첫 번째 단어의 연결을 확인
        if words[-1][-1] != words[0][0]:
            return False
        
        return True