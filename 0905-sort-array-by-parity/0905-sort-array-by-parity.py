class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # 두 개의 포인터를 사용하여 배열을 조정
        # i는 배열의 시작부터, j는 배열의 끝에서 시작
        i, j = 0, len(nums) - 1
        
        # i가 j보다 작은 동안만 반복
        while i < j:
            # nums[i]가 짝수이면 i를 증가시킴
            while i < j and nums[i] % 2 == 0:
                i += 1
            # nums[j]가 홀수이면 j를 감소시킴
            while i < j and nums[j] % 2 == 1:
                j -= 1
                
            # i와 j 위치의 요소 교환
            nums[i], nums[j] = nums[j], nums[i]
            
        return nums