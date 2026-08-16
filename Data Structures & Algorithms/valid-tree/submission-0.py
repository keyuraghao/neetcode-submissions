from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # the meaning of a valid tree means that the edges of the node does not form a cycle 

        # code snippet make a adj list
        neighbours = [[] for _ in range(n+1)]
        for u,v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)

        parent = [0] * (n+1) # a list that maintains the parent of the nodes
        visited = [False] * (n+1) # list to maintain the visited node so that we do not stuck in a loop
        trees = 0 # lets count the number of trees 

        for node in range(n): # since the node are from 0 -> n-1 we are going though each node
            if visited[node]: # if the node is alreay visited we do not need to mark it for a new start because there can be a case of disconnected trees
                continue

            trees += 1 # beacuse we complete one entire tree in one go with the help of BFS  
            parent[node] = -1 # lets consider this is the base or the root node
            visited[node] = True # marking the node visited so that we are not stuck in a loop because of undirected graph
            q = deque() # initializing the queue for BFS
            q.append(node) # appendng the root node as the start of the queue

            # starting normal BFS
            while q:
                q_node = q.popleft() # get the node
                for neighbour in neighbours[q_node]: # for all of the nodes neighbours
                    if not visited[neighbour]: # if the neighbours are not visted then
                        visited[neighbour] = True # visit the neighbour
                        parent[neighbour] = q_node # set the parent of the neighbour to the node
                        q.append(neighbour) # append it to the q for further bfs
                    elif parent[q_node] != neighbour: # now we have encountered a situatuion where the node is visited, there can be 2 possiblities either the parent is the current node (i.e.) there is no issue of the cycle or else the parent of the node is not the neighbour which means there is another edge coming to this node this means there is a cycle 
                        return False
        return trees == 1 # if there is only one tree then true else false beause there can be multiple trees which are not collected ans we are asked for a single tree
