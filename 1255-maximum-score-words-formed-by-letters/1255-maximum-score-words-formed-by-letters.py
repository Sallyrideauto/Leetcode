class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # 글자별 점수 계산
        def word_score(word):
            total_score = 0
            word_count = collections.Counter(word)
            # 글자 점수 누적 확인
            for char, cnt in word_count.items():
                total_score += score[ord(char) - ord('a')] * cnt
            return total_score
        
        # 백트래킹 함수
        def backtrack(index, current_score, letter_count):
            nonlocal max_score
            # 현재 점수가 최대 점수보다 크면 갱신
            max_score = max(max_score, current_score)
            
            # 더 이상 고려할 단어가 없으면 반환
            if index == len(words):
                return
            
            # 현재 단어 사용 가능한지 체크
            word = words[index]
            word_count = collections.Counter(word)
            can_use = True
            for char, cnt in word_count.items():
                if letter_count[char] < cnt:
                    can_use = False
                    break
                    
            if can_use:
                for char, cnt in word_count.items():
                    letter_count[char] -= cnt
                backtrack(index + 1, current_score + word_score(word), letter_count)
                # 사용 후 복원
                for char, cnt in word_count.items():
                    letter_count[char] += cnt
                    
            # 현재 단어를 사용하지 않는 경우
            backtrack(index + 1, current_score, letter_count)
            
        # 초기 글자 카운트
        letter_count = collections.Counter(letters)
        max_score = 0
        
        # 백트래킹 시작
        backtrack(0, 0, letter_count)
        
        return max_score