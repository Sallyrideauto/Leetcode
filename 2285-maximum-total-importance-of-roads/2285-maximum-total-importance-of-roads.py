class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # 도시별 도로 연결 수 계산
        frequency = [0] * n
        for u, v in roads:
            frequency[u] += 1
            frequency[v] += 1
        
        # 중요도 할당을 위해 도시들을 도로 연결 수에 따라 정렬
        importance = sorted(range(n), key=lambda x: frequency[x], reverse = True)
        
        # 중요도 할당(가장 중요한 도시부터 n 부여)
        city_importance = [0] * n
        for i in range(n):
            city_importance[importance[i]] = n - i
            
        # 모든 도로의 중요도 합 계산
        total_importance = 0
        for u, v in roads:
            total_importance += city_importance[u] + city_importance[v]
            
        return total_importance