class Solution:
    def rev(self, x):   # rev 메서드에 self 매개변수 추가
        # 정수 x를 문자열로 반환 후 뒤집고, 다시 정수로 변환
        return int(str(x)[::-1])
    
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        count = 0
        freq = {}
        
        for num in nums:
            # nums[i] - rev(nums[i])의 값 계산
            diff = num - self.rev(num)
            # 이 차이값을 key로 사용하여 freq 딕셔너리에 빈도수를 기록
            if diff in freq:
                # 이미 존재하는 차이값에 대해서는 nice 쌍의 개수 증가
                count = (count + freq[diff]) % MOD
            freq[diff] = freq.get(diff, 0) + 1
            
        return count