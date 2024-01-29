#User function Template for python3

class Solution:
    def TotalCount(self, s):
        # Code here
        n=len(s) #Get the length of the string
        maxl=100 #Set the maximum length for dp array
        dp=[[-1 for i in range(9*maxl+1)] for i in range(maxl)] #Initialize dp array with -1

        # Define a recursive helper function
        def helper(p,psum):
            if p==n: # If we have reached the end of the string
                return 1 # Return 1 to indicate a valid combination
            if dp[p][psum]!=(-1): # If the value is already evaluated
                return dp[p][psum] # Return the stored value

            ans=0
            sumd=0
            dp[p][psum]=0

            # Iterate over the string starting from position p
            for i in range(p,n):
                sumd+=int(s[i]) # Calculate the sum of digits from position p to i
                if sumd>=psum: # If the sum is greater than or equal to psum
                    ans+=helper(i+1,sumd) # Recursively call the helper function
            dp[p][psum]=(ans) # Store the result in dp array
            return dp[p][psum] # Return the result

        return helper(0,0) 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.TotalCount(s)
		print(ans)
# } Driver Code Ends