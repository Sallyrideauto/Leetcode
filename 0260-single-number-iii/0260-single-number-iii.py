class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 모든 숫자의 XOR을 계산
        xor = 0
        for num in nums:
            xor ^= num
        
        # xor 결과에서 첫 번째로 1이 나타나는 위치를 찾기
        diff = xor & -xor   # xor에서 가장 낮은 1비트 추출
        
        # 두 그룹으로 나누어 XOR 계산
        x = 0
        y = 0
        for num in nums:
            if num & diff:  # 해당 비트가 1인 경우
                x ^= num
            else:   # 해당 비트가 0인 경우
                y ^= num
                
        return [x, y]