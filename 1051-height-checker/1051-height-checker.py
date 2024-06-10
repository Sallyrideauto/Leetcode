class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)  # 원래 배열을 정렬하여 새로운 배열 생성
        mismatch_count = 0
        
        for original, sorted_height in zip(heights, expected):
            if original != sorted_height:
                mismatch_count += 1 # 원본과 정렬된 배열을 비교하여 다른 경우 카운트 증가
        
        return mismatch_count