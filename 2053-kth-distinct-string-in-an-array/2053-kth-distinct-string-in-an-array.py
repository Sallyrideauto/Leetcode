from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # 각 문자열의 빈도 계산
        freq = Counter(arr)
        
        # distinct한 문자열 리스트 생성
        distinct_strings = [string for string in arr if freq[string] == 1]
        
        # k번째 distinct한 문자열 출력(k는 1-based index이므로 0-based로 변환)
        if k <= len(distinct_strings):
            return distinct_strings[k - 1]
        else:
            return ""   # k번째 distinct한 문자열이 없는 경우 빈 문자열 출력