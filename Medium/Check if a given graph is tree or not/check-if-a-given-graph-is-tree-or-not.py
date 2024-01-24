#User function Template for python3

from collections import deque

class Solution:
    def isTree(self, n, m, edges):
        if m != n - 1:
            return 0

        vis = [False] * n
        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        node = 0
        q = deque()

        vis[node] = True
        visited = 1
        q.append(node)

        while q:
            curr = q.popleft()
            for neighbor in adj[curr]:
                if not vis[neighbor]:
                    vis[neighbor] = True
                    visited += 1
                    q.append(neighbor)

        return int(visited == n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range (int(input())):
    n,m = [int(i) for i in input().split()]
    edges = []
    for i in range(m):
        a,b = map(int,input().split())
        edges.append([a,b])

    ob = Solution()
    print(ob.isTree(n,m,edges))
# } Driver Code Ends