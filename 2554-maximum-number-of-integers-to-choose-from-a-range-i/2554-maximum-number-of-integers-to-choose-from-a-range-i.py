class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # 1부터 n까지의 모든 수 중에서 banned에 없는 수를 선택
        available_numbers = set(range(1, n + 1)) - set(banned)
        
        # 사용 가능한 숫자들을 리스트로 정렬
        sorted_numbers = sorted(available_numbers)
        
        current_sum = 0
        count = 0
        
        # 작은 수부터 더하면서 최대 합을 넘지 않도록 함
        for number in sorted_numbers:
            if current_sum + number <= maxSum:
                current_sum += number
                count += 1
            else:
                break
        
        return count