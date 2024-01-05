#User function Template for python3

class Solution:
    def TotalWays(self, N):
        # initializing two arrays for storing the number of ways to reach
        # the current step with an odd or even number of steps taken
        # dpO stores the number of ways with an odd number of steps
        # dpI stores the number of ways with an even number of steps
        dpO=[0 for _ in range(0,N)]
        dpI=[0 for _ in range(0,N)]

        # there is only one way to reach the first step, so set both dpO[0] and dpI[0] to 1
        dpO[0]=1
        dpI[0]=1

        # we need to take modulo with a large number to avoid integer overflow
        mod=10**9+7

        # iterate from 1 to N-1 to calculate the number of ways for each step
        for i in range(1,N):
            # the number of ways to reach the current step with an odd number of steps
            # is equal to the sum of the number of ways to reach the previous step with an odd number of steps
            # and the number of ways to reach the previous step with an even number of steps
            dpO[i]=(dpO[i-1]+dpI[i-1])%mod

            # the number of ways to reach the current step with an even number of steps
            # is equal to the number of ways to reach the previous step with an odd number of steps
            dpI[i]=dpO[i-1]
        
        # the total number of ways to reach the Nth step is the sum of the number of ways to reach the Nth step
        # with an odd number of steps and the number of ways to reach the Nth step with an even number of steps
        # we need to take modulo with a large number to avoid integer overflow
        return ((dpO[N-1] + dpI[N-1])%mod*(dpO[N-1] + dpI[N-1])%mod)%mod

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends