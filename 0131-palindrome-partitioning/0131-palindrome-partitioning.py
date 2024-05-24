from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub: str) -> bool:
            # 양 끝에서 시작해서 중앙으로 이동하면서 팰린드롬인지 확인
            return sub == sub[::-1]
        
        def backtrack(start: int, path: List[str]):
            # 문자열의 끝에 도달하면 하나의 팰린드롬 분할 완성
            if start == len(s):
                results.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                # start부터 end-1까지 부분 문자열
                if is_palindrome(s[start:end]):
                    # 팰린드롬이면 현재 path에 추가하고 계속 탐색
                    backtrack(end, path + [s[start:end]])
                
        results = []
        backtrack(0, [])
        return results