class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0    # nums1의 모든 요소를 XOR한 값
        xor2 = 0    # nums2의 모든 요소를 XOR한 값

        # nums1, nums2 전체를 각각 XOR
        for num in nums1:
            xor1 ^= num
        for num in nums2:
            xor2 ^= num

        # 결과 계산
        # nums1 길이가 홀수일 때 nums2 전체 XOR
        # nums2 길이가 홀수일 때 nums1 전체 XOR
        result = 0
        if len(nums1) % 2 == 1:
            result ^= xor2
        if len(nums2) % 2 == 1:
            result ^= xor1

        return result