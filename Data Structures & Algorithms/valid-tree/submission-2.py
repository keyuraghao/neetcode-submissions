class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # doing the same thing using dfs algorithm

        neighbours = [[] for _ in range(n+1)]

        for u,v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)

        visited = [False] * (n+1)

        def dfs(node,parent):
            visited[node] = True
            for neighbour in neighbours[node]:
                if not visited[neighbour]:
                    if dfs(neighbour,parent=node):
                        return True
                elif neighbour != parent:
                    return True
            return False

        trees = 0
        for node in range(n):
            if not visited[node]:
                trees += 1
                if dfs(node,parent=-1):
                    return False
        return trees == 1