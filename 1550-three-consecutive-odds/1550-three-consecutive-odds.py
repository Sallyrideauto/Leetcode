class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # 배열의 길이 확인
        n = len(arr)
        # 연속된 세 개의 홀수를 찾기 위해 n-2까지 순회
        for i in range(n - 2):
            # 연속된 세 수가 모두 홀수인지 확인
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        # 연속된 세 개의 홀수를 찾지 못했다면 False 반환
        return False