class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = [] # 결과를 저장할 리스트

        # 각 단어를 다른 단어와 비교
        for i in range(len(words)):
            for j in range(len(words)):
                # 자기 자신은 비교 대상에서 제외
                if i != j and words[i] in words[j]:
                    # 하위 문자열이면 결과에 추가
                    result.append(words[i])
                    break   # 중복 방지를 위해 한 번 발견되면 중단

        return result