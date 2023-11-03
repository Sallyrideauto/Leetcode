'''
Logic Explanation:

1. For each number t in target, we need to consider numbers from the current number in the stream num up to t.
2. We push each number to the stack and add a "Push" operation.
3. If the current number in the stream is not in the target, 
   we pop it from the stack and add a "Pop" operation.
4. We continue this process until we have gone through all the numbers in target.
'''

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # Initialize an empty list to store the operations
        operations = []
        # Initialize an empty stack
        stack = []
        # Initialize a counter for the current number in the stream
        num = 1
        for t in target:
            while num <= t:
                # Push the current number to the stack
                stack.append(num)
                # Add "Push" to the operations
                operations.append("Push")
                # If the current number is not in the target, pop it and add "Pop" to the operations
                if num not in target:
                    stack.pop()
                    operations.append("Pop")
                # Move to the next number in the stream
                num += 1
        return operations