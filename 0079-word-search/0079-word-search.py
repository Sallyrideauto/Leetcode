class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS 함수인 dfs는 현재 위치 (i, j)와 현재 탐색 중인 단어의 인덱스 k를 매개변수로 받습니다.
        def dfs(i, j, k):
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
                return False
                # 현재 위치 (i, j)가 그리드 범위를 벗어나거나 현재 위치의 문자가 현재 탐색 중인 단어의 문자와 다르면 False를 반환합니다.
            if k == len(word) - 1:
                return True
                # 현재 탐색 중인 단어의 인덱스가 단어의 길이와 같으면 (즉, 모든 문자를 찾았으면) True를 반환합니다.
            tmp, board[i][j] = board[i][j], '/'
            # 현재 위치의 문자를 임시 변수에 저장하고, 현재 위치의 문자를 '/'로 변경합니다. 이렇게 함으로써 같은 문자를 두 번 이상 사용하지 않도록 합니다.
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # 상하좌우 방향으로 DFS를 재귀적으로 호출하여 단어를 찾습니다.
            board[i][j] = tmp
            # DFS 호출이 완료되면 이전에 변경한 문자를 다시 원래대로 되돌립니다.
            return res
            
        # 모든 그리드 위치에 대해 DFS를 호출하여 단어를 찾습니다. 만약 단어를 찾으면 True를 반환하고, 찾지 못하면 False를 반환합니다.
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
                
        return False
