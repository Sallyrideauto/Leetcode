class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()   # 사람들의 무게를 정렬
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1   # 더 가벼운 사람도 함께 태우고
            right -= 1  # 가장 무거운 사람을 태움
            boats += 1  # 보트 수 증가
            
        return boats