class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # 'ch'가 'word'에서 나타나는 첫 번째 위치를 찾기
        index = word.find(ch)
        
        # 'ch'가 'word'에 존재하지 않는다면 그대로 반환
        if index == -1:
            return word
        
        # 'ch'가 나타나는 위치까지의 부분을 뒤집은 다음, 뒤집힌 부분과 나머지 부분 합치기
        return word[:index + 1][::-1] + word[index + 1:]