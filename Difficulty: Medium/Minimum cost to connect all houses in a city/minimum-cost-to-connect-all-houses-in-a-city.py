class DSU:

    def __init__(self, n):
        # Initialize parent and rank arrays
        self.parent = [-1] * n
        self.rank = [1] * n

    # Find function with path compression
    def find(self, i):
        if self.parent[i] == -1:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Union function with union by rank
    def unite(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)

        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1


# Graph class to build and process edges
class Graph:

    def __init__(self, V):
        self.V = V
        self.edgelist = []

    # Adds an edge between house u and house v with given cost
    def addEdge(self, x, y, w):
        self.edgelist.append((w, x, y))

    # Runs Kruskal's algorithm to return the MST total cost
    def kruskalsMST(self):

        # Sort edges based on weight
        self.edgelist.sort()
        s = DSU(self.V)

        # Total cost of MST
        ans = 0

        # Number of edges included in MST
        count = 0

        for w, x, y in self.edgelist:

            # Include edge if it doesn't form a cycle
            if s.find(x) != s.find(y):
                s.unite(x, y)
                ans += w
                count += 1

            # If MST contains V - 1 edges, stop
            if count == self.V - 1:
                break

        return ans


class Solution:

    def minCost(self, houses):
        n = len(houses)
        g = Graph(n)

        # Add edges between every pair of houses with
        # Manhattan distance as cost
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] -
                                                              houses[j][1])
                g.addEdge(i, j, cost)

        # Compute MST cost
        return g.kruskalsMST()


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []

        for _ in range(n):
            temp = list(map(int, input().split()))
            edges.append(temp)

        obj = Solution()
        print(obj.minCost(edges))
        print("~")
# } Driver Code Ends