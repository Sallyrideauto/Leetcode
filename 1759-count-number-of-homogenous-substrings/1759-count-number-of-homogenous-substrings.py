class Solution:
    def countHomogenous(self, s: str) -> int:
        # Define the module value.
        MOD = 10 ** 9 + 7
        
        # Initialize the current count and the total count.
        count = 1   # We start with 1 becsuse the first character itself is a homogeneous substring.
        total = 0
        
        # Iterate through the string starting from the second character.
        for i in range(1, len(s)):
            # If the current character is the same as the previous one,
            # increase the count.
            if s[i] == s[i - 1]:
                count += 1
            else:
                # If the current character is different,
                # add the number of homogenous substring of the previous sequence to the total.
                total += count * (count + 1) // 2
                
                # Reset count for the new character.
                count = 1
            
            # Ensure the total is within the modulo range.
            total %= MOD
            
        # Add the homogenous substrings from the last sequence if identical characters.
        total += count * (count + 1) // 2
        total %= MOD    # Ensure the total is within the modulo range.
        
        return total