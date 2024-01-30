#User function Template for python3

class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        memo=[[[-1]*(n3+1) 
                for i in range(n2+1)] 
                for  i in range(n1+1)]
                
        return self.solve(A,B,C,0,0,0,n1,n2,n3,memo)
        
    def solve(self,A,B,C,i,j,k,n1,n2,n3,memo):
        if (i == n1 or j == n2 or k == n3):
            return 0;

        if (memo[i][j][k] != -1):
            return memo[i][j][k];
    
        # if all the characters are same, we can include them in the longest length
        # and check for the longest length in state (i + 1, j + 1, k + 1)
        if (A[i] == B[j] and A[i] == C[k]):
            memo[i][j][k] = 1 + self.solve (A, B, C, i + 1, j + 1, k + 1, n1, n2, n3,memo);
            return memo[i][j][k]
    
        # if the characters do not match, we simply call for all the possible recursions
        # and store the maximum we get out of them
        memo[i][j][k] = max (self.solve (A, B, C, i + 1, j, k, n1, n2, n3,memo),
                                     self.solve (A, B, C, i, j + 1, k, n1, n2, n3,memo),
                                     self.solve (A, B, C, i, j, k + 1, n1, n2, n3,memo))
        return memo[i][j][k]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n1,n2,n3 = map(int,input().split())
        A,B,C = input().split()

        solObj = Solution()

        ans = solObj.LCSof3(A,B,C,n1,n2,n3)

        print(ans)
# } Driver Code Ends