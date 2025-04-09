class Solution:

    def dfs(self, adj, c, visited):
        visited[c] = True
        for neighbor in adj[c]:
            if not visited[neighbor]:
                self.dfs(adj, neighbor, visited)

    def constructadj(self, V, edges, c, d):
        adj = [[] for _ in range(V)]
        for a, b in edges:
            if (a == c and b == d) or (a == d and b == c):
                continue
            adj[a].append(b)
            adj[b].append(a)
        return adj

    def isBridge(self, V, edges, c, d):
        adj = self.constructadj(V, edges, c, d)
        visited = [False] * V
        self.dfs(adj, c, visited)
        return not visited[d]



#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]
        edges = []

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append([u, v])

        c = int(input())
        d = int(input())

        obj = Solution()
        l = obj.isBridge(V, edges, c, d)

        if l:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends