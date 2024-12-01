class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # 집합을 생성하여 이미 본 숫자를 저장
        seen = set()
        
        # 배열의 각 원소를 순회
        for num in arr:
            # 현재 숫자의 두 배가 이미 집합에 존재하는지 확인
            if 2 * num in seen:
                return True
            
            # 현재 숫자가 짝수일 경우, 그 절반이 집합에 존재하는지 확인
            if num % 2 == 0 and num // 2 in seen:
                return True
            
            # 현재 숫자를 집합에 추가
            seen.add(num)
            
        # 배열들을 모두 순회한 후에도 조건을 만족하는 쌍이 없다면 False를 반환
        return False