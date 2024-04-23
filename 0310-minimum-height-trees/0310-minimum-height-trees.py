class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                j = adj[leaf].pop()
                adj[j].remove(leaf)
                if len(adj[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves