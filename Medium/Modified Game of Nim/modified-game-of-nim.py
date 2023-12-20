#User function Template for python3

class Solution:
    def findWinner(self, n, A):
        res = 0
        for i in range(n):
            res ^= A[i]
        
        # when player 1 wins
        if res == 0 or n % 2 == 0:
            return 1
        
        # when player 2 wins
        else:
            return 2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        A = input().split()
        for itr in range(n):
            A[itr] = int(A[itr])

        ob = Solution()
        print(ob.findWinner(n, A))

# } Driver Code Ends