import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        for i in range(n):
            for j in range(i + 1, n):
                heapq.heappush(heap, (arr[i] / arr[j], i, j))
            
        # k-1번만큼 합에서 원소를 제거하고, k번째 원소 반환
        for _ in range(k - 1):
            heapq.heappop(heap)
            
        value, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]