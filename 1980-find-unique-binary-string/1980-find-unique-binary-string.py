class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # nums에 포함되지 않는 이진 문자열을 찾기 위해 
        # nums를 집합으로 변환하여 빠른 검색이 가능하도록 함
        num_set = set(nums)
        
        # 가능한 모든 이진 문자열 생성
        # n의 최대 크기가 16이므로, 이 방법은 실행 가능함
        n = len(nums[0])
        for i in range(2 ** n):
            # i를 2진수 문자열로 변환
            bin_str = format(i, 'b').zfill(n)
            # 만약 이 이진 문자열이 nums에 없다면 반환
            if bin_str not in num_set:
                return bin_str