class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # 전체 XOR 값 계산
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            
        # 목표 XOR 값 정의
        max_xor = (1 << maximumBit) - 1 # 2^maximumBit - 1
        
        # 결과 배열 생성
        result = []
        for num in reversed(nums):
            result.append(xor_sum ^ max_xor)    # 최대 XOR 값 추가
            xor_sum ^= num  # 오른쪽 끝부터 XOR 값 갱신
            
        return result