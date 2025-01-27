from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 그래프 초기화
        reachable = [[False] * numCourses for _ in range(numCourses)]

        # 직접적인 선후 관계 설정
        for pre, course in prerequisites:
            reachable[pre][course] = True

        # 플로이드-워셜 알고리즘 적용
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])

        # 쿼리 처리
        result = []
        for pre, course in queries:
            result.append(reachable[pre][course])

        return result