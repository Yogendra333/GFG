class Solution:

    # Build adjacency list from edge list
    @staticmethod
    def constructAdj(V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return adj

    # Helper function to perform DFS and find articulation points
    # using Tarjan's algorithm.
    @staticmethod
    def findPoints(adj, u, visited, disc, low, time, parent, isAP):
        # Mark vertex u as visited and assign discovery
        # time and low value
        visited[u] = 1
        time[0] += 1
        disc[u] = low[u] = time[0]
        children = 0

        # Process all adjacent vertices of u
        for v in adj[u]:
            # If v is not visited, then recursively visit it
            if not visited[v]:
                children += 1
                Solution.findPoints(adj, v, visited, disc, low, time, u, isAP)

                # Check if the subtree rooted at v has a
                # connection to one of the ancestors of u
                low[u] = min(low[u], low[v])

                # If u is not a root and low[v] is greater than or equal to disc[u],
                # then u is an articulation point
                if parent != -1 and low[v] >= disc[u]:
                    isAP[u] = 1

            # Update low value of u for back edge
            elif v != parent:
                low[u] = min(low[u], disc[v])

        # If u is root of DFS tree and has more than
        # one child, it is an articulation point
        if parent == -1 and children > 1:
            isAP[u] = 1

    # Main function to find articulation points in the graph
    def articulationPoints(self, V, edges):
        adj = Solution.constructAdj(V, edges)
        disc = [0] * V
        low = [0] * V
        visited = [0] * V
        isAP = [0] * V
        time = [0]

        # Run DFS from each vertex if not
        # already visited (to handle disconnected graphs)
        for u in range(V):
            if not visited[u]:
                Solution.findPoints(adj, u, visited, disc, low, time, -1, isAP)

        # Collect all vertices that are articulation points
        result = [u for u in range(V) if isAP[u]]

        # If no articulation points are found, return list containing -1
        return result if result else [-1]

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(int(1e7))


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append([u, v])
        obj = Solution()
        ans = obj.articulationPoints(V, edges)
        ans.sort()
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends