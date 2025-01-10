class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0 # 결과 저장 변수 초기화

        # words 리스트 순회
        for word in words:
            # 단어가 pref로 시작하면 cnt 증가
            if word.startswith(pref):
                cnt += 1

        # 최종 카운트 반환
        return cnt