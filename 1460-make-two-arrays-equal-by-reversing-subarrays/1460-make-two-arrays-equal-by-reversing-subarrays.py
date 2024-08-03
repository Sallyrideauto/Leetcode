class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_sorted = sorted(target)
        arr_sorted = sorted(arr)
        
        return target_sorted == arr_sorted