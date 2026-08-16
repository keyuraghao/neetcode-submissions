from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbours = [[] for _ in range(n+1)]
        for u,v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)

        parent = [0] * (n+1)
        visited = [False] * (n+1)

        connected_components = 0

        for node in range(n):
            if visited[node]:
                continue
            
            connected_components += 1
            q = deque()
            q.append(node)
            visited[node] = True
            parent[node] = -1
            while q:
                q_node = q.popleft()
                for neighbour in neighbours[q_node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        q.append(neighbour)
                        parent[neighbour] = q_node
                    # elif parent[q_node] != neighbour:
                    #     return False

        return connected_components