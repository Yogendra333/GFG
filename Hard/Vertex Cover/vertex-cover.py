from typing import List


class Solution:
    def checkCover(self, n, k, m, e):
        # Set has first 'k' bits high initially
        set_val = (1 << k) - 1
    
        limit = (1 << n)
    
        # To mark the edges covered in each subset of size 'k'.
    
        while set_val < limit:
            visited = [[False] * (n + 1) for _ in range(n + 1)]
    
            # Set counter for number of edges covered from this subset of vertices to zero.
            cnt = 0
    
            # Selected vertex cover is the indices where 'set_val' has its bit high.
            v = 1
            j = 1
            while j<limit:
                # v = 1 << (j - 1)
                if set_val & j:
                    # Mark all edges emerging out of this vertex as visited
                    for k in range(1, n + 1):
                        if e[v][k] and not visited[v][k]:
                            visited[v][k] = True
                            visited[k][v] = True
                            cnt += 1
                
                j <<= 1
                v += 1
    
            # If the current subset covers all the edges
            if cnt == m:
                return True
    
            # Generate next combination with k set bits
            c = set_val & -set_val
            r = set_val + c
            set_val = (((r ^ set_val) >> 2) // c) | r
        
        return False

    def vertexCoverHelper(self, e, n, m):
        # Binary search the answer.
        low, high = 1, n
    
        while high > low:
            mid = (low + high) >> 1
    
            if not self.checkCover(n, mid, m, e):
                low = mid + 1
            else:
                high = mid
        
        return low

    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        m = len(edges)

        e = [[0] * (n + 1) for _ in range(n + 1)]

        # Push the adjacent nodes for each node.
        for i in range(m):
            e[edges[i][0]][edges[i][1]] = 1
            e[edges[i][1]][edges[i][0]] = 1
        
        return self.vertexCoverHelper(e, n, m)
        



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        
        edges=IntMatrix().Input(m, m)
        
        obj = Solution()
        res = obj.vertexCover(n, edges)
        
        print(res)
        

# } Driver Code Ends