class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)  # 모든 학생의 분필 사용량 합
        k %= total  # 완전한 사이클을 반복하고 남은 분필의 양
        
        # 각 학생을 순회하면서 남은 분필의 양으로 충분하지 않을 때의 학생 인덱스 반환
        for i, usage in enumerate(chalk):
            if k < usage:
                return i
            k -= usage
            
        return -1   # 이 부분은 실제로 도달하지 않음, 모든 경우를 커버