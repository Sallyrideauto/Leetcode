class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, current_xor):
            if index == len(nums):
                return current_xor
            # 현재 요소를 포함하는 경우
            include = backtrack(index + 1, current_xor ^ nums[index])
            # 현재 요소를 포함하지 않는 경우
            exclude = backtrack(index + 1, current_xor)
            return include + exclude
        
        # 시작점: 0번 인덱스, 현재 XOR 값은 0
        return backtrack(0, 0)