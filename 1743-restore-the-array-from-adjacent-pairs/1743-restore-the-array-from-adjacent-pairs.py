'''
이 문제를 해결하기 위해 우리는 해시 테이블을 사용하여 인접한 쌍을 저장하고 배열을 재구성하는 방법을 사용할 것입니다. 접근 방법은 다음과 같습니다:
1. 인접한 쌍을 저장하기 위해 해시 맵을 만듭니다. 각 숫자는 해당 숫자와 인접한 숫자들의 리스트를 가집니다.
2. 시작 요소를 찾기 위해 해시 맵을 검사합니다. 시작 요소는 인접한 숫자가 하나뿐인 유일한 요소입니다.
3. 시작 요소부터 시작하여, 각 단계에서 현재 요소의 인접한 요소를 찾고 결과 배열에 추가합니다.
4. 이미 방문한 요소를 표시하여 같은 요소를 반복하지 않도록 합니다.
'''

from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # 인접한 쌍을 저장하기 위한 해시 테이블 생성
        adj_map = defaultdict(list)
        for a, b in adjacentPairs:
            adj_map[a].append(b)
            adj_map[b].append(a)
            
        # 시작 요소 찾기(인접한 요소가 하나뿐인 요소)
        for key in adj_map:
            if len(adj_map[key]) == 1:
                start = key
                break
                
        # 결과 배열 초기화 및 시작 요소 추가
        result = [start]
        
        # 이전 요소 표시
        prev = None
        
        # 결과 배열 생성
        while len(result) < len(adjacentPairs) + 1:
            current = result[-1]
            next_elements = adj_map[current]
            
            # 다음 요소 찾기(이전에 방문하지 않은 요소)
            for next_element in next_elements:
                if next_element != prev:
                    result.append(next_element)
                    prev = current
                    break
                    
        return result