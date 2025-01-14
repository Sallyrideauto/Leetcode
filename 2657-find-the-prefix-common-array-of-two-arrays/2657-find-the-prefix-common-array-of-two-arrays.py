class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # 공통 원소 수를 저장할 결과 리스트
        result = []
        # 두 배열에서 등장한 원소를 저장할 집합
        setA, setB = set(), set()

        # 두 배열을 prefix로 순회
        for a, b in zip(A, B):
            setA.add(a) # A의 현재 원소 추가
            setB.add(b) # B의 현재 원소 추가
            # 현재까지의 공통 원소 개수를 계산
            common_count = len(setA & setB)
            result.append(common_count)

        return result