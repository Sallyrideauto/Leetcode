class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # 자릿수 합을 계산하는 함수
        def digit_sum(num: int) -> int:
            s = 0
            while num:
                s += num % 10
                num //= 10
            return s
        
        answer = -1  # 최대 합을 저장할 변수, 초기값은 두 수를 찾지 못한 경우 -1
        # 자릿수 합을 key로, 해당 그룹에서 현재까지의 최댓값을 value로 저장하는 딕셔너리
        digit_sum_to_max = {}
        
        # 배열의 각 숫자에 대해 처리
        for num in nums:
            d_sum = digit_sum(num)  # 현재 숫자의 자릿수 합 계산
            # 이미 같은 자릿수 합을 가진 숫자가 존재한다면, 두 수의 합을 후보로 계산
            if d_sum in digit_sum_to_max:
                answer = max(answer, num + digit_sum_to_max[d_sum])
            # 해당 자릿수 합 그룹에서 현재까지의 최댓값 갱신
            digit_sum_to_max[d_sum] = max(num, digit_sum_to_max.get(d_sum, 0))
        
        return answer
