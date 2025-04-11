class Solution:

    def constructAdj(self, edges, V):

        # adj[u] = list of [v, wt]
        adj = [[] for _ in range(V)]

        for edge in edges:
            u, v, wt = edge
            adj[u].append([v, wt])
            adj[v].append([u, wt])

        return adj

    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # Create adjacency list
        adj = self.constructAdj(edges, V)

        # Create a priority queue to store vertices that
        # are being preprocessed.
        pq = []

        # Create a list for distances and initialize all
        # distances as infinite
        dist = [sys.maxsize] * V

        # Insert source itself in priority queue and initialize
        # its distance as 0.
        heapq.heappush(pq, [0, src])
        dist[src] = 0

        # Looping till priority queue becomes empty (or all
        # distances are not finalized)
        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            u = heapq.heappop(pq)[1]

            # Get all adjacent of u.
            for x in adj[u]:
                # Get vertex label and weight of current
                # adjacent of u.
                v, weight = x[0], x[1]

                # If there is shorter path to v through u.
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, [dist[v], v])

        # Return the shortest distance array
        return dist


#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import heapq

# Position this line where user code will be pasted.


def main():
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
            edges.append([v, u, w])  # Since the graph is undirected

        src = int(input())

        obj = Solution()
        res = obj.dijkstra(V, edges, src)

        print(" ".join(map(str, res)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends