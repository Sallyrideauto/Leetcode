class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # 누적 XOR 배열 생성
        prefix = [0] * (len(arr) + 1)
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] ^ arr[i - 1]
            
        # 쿼리 결과 계산
        result = []
        for l, r in queries:
            if l == 0:
                result.append(prefix[r + 1])
            else:
                result.append(prefix[r + 1] ^ prefix[l])
                
        return result