class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        visited = [False] * n
        depth = [-1] * n
        longest_cycle = 0
        two_cycle_sum = 0
        
        # Helper function to find cycles
        def find_cycle_length(node):
            nonlocal longest_cycle
            stack = []
            current_depth = 0
            while True:
                if visited[node]:
                    if depth[node] != -1:
                        # Cycle length
                        longest_cycle = max(longest_cycle, current_depth - depth[node])
                    return
                visited[node] = True
                depth[node] = current_depth
                stack.append(node)
                current_depth += 1
                node = favorite[node]
        
        # Process all nodes to find cycles
        for i in range(n):
            if not visited[i]:
                find_cycle_length(i)
        
        # Reset visited and depth for two-cycle trees processing
        visited = [False] * n
        def find_tree_length(node, exclude):
            max_depth = 0
            stack = [(node, 0)]
            while stack:
                current, current_depth = stack.pop()
                visited[current] = True
                max_depth = max(max_depth, current_depth)
                for neighbor in range(n):
                    if neighbor != exclude and not visited[neighbor] and favorite[neighbor] == current:
                        stack.append((neighbor, current_depth + 1))
            return max_depth
        
        # Process two-way cycles
        for i in range(n):
            if favorite[favorite[i]] == i and i < favorite[i]:
                # i and favorite[i] form a two-way cycle
                visited[i] = visited[favorite[i]] = True
                left_tree = find_tree_length(i, favorite[i])
                right_tree = find_tree_length(favorite[i], i)
                two_cycle_sum += left_tree + right_tree + 2
        
        return max(longest_cycle, two_cycle_sum)
