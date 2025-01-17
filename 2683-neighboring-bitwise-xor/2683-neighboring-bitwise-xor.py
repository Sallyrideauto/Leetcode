class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)    # 길이를 구함

        # 첫 번째 가정: original[0] = 0
        original_0 = [0]
        for i in range(n - 1):
            original_0.append(original_0[-1] ^ derived[i])
        if original_0[0] ^ original_0[-1] == derived[-1]:
            return True

        # 두 번째 가정: original[0] = 1
        original_1 = [1]
        for i in range(n - 1):
            original_1.append(original_1[-1] ^ derived[i])
        if original_1[0] ^ original_1[-1] == derived[-1]:
            return True

        # 둘 다 실패한 경우
        return False