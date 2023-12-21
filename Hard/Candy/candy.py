#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minCandy(self, N, ratings):
        #Initializing a list c with 1s to represent the minimum number of candies for each child.
        c = [1] * N
        
        #Looping through each child starting from the second one.
        for i in range(1, N):
            #Comparing the current child's rating with the previous one.
            #If the current rating is greater, assign one more candy than the previous child.
            if ratings[i] > ratings[i-1]:
                c[i] = c[i-1] + 1
        
        #Looping through each child starting from the second last one.
        for i in range(N-2, -1, -1):
            #Comparing the current child's rating with the next one.
            #If the current rating is greater, assign maximum between the current value and the next child's value plus 1.
            if ratings[i] > ratings[i+1]:
                c[i] = max(c[i], c[i+1] + 1)
        
        #Calculating the total number of candies required by summing up the values in the c list.
        res = 0
        for t in c:
            res += t
        
        #Returning the total number of candies required.
        return res

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ratings = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCandy(N, ratings)
        print(res)
# } Driver Code Ends