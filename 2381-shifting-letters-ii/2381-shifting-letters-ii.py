class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Step 1: Initialize difference array
        n = len(s)
        shift_delta = [0] * (n + 1)
        
        # Step 2: Process each shift operation
        for start, end, direction in shifts:
            if direction == 1:  # Right shift
                shift_delta[start] += 1
                shift_delta[end + 1] -= 1
            else:  # Left shift
                shift_delta[start] -= 1
                shift_delta[end + 1] += 1
        
        # Step 3: Calculate prefix sum to get final shift values
        shift_sum = 0
        final_shifts = [0] * n
        for i in range(n):
            shift_sum += shift_delta[i]
            final_shifts[i] = shift_sum
        
        # Step 4: Apply shifts to the string
        result = []
        for i, char in enumerate(s):
            # Calculate new character with modular arithmetic
            new_char = chr((ord(char) - ord('a') + final_shifts[i]) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)
