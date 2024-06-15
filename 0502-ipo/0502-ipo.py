import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 프로젝트를 자본에 따라 정렬
        projects = sorted(zip(capital, profits))
        max_heap = []
        j = 0
        
        # 최대 k번의 프로젝트를 선택
        for _ in range(k):
            # 현재 자본으로 가능한 모든 프로젝트를 힙에 푸시
            while j < len(projects) and projects[j][0] <= w:
                heapq.heappush(max_heap, -projects[j][1])
                j += 1
                
            # 수익이 가장 큰 프로젝트를 힙에서 제거하고 자본에 추가
            if max_heap:
                w -= heapq.heappop(max_heap)    # 수익을 음수로 저장했기 때문에 빼는 것이 아니라 더해짐
            else:
                # 더 이상 선택할 수 있는 프로젝트가 없다면 종료
                break
                
        return w