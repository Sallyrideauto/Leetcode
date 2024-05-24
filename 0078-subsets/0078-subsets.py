class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        
        def backtrack(start):
            # 현재 subset을 결과에 추가
            result.append(subset.copy())
            
            for i in range(start, len(nums)):
                # 현재 숫자를 subset에 추가
                subset.append(nums[i])
                # 재귀적으로 다음 원소를 추가
                backtrack(i + 1)
                # 백트래킹을 위해 마지막 원소 제거
                subset.pop()
                
        backtrack(0)
        return result