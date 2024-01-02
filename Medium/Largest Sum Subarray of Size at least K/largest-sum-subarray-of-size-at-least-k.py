#User function Template for python3

class Solution():
    def maxSumWithK(self, a, n, k):
    
        ans=-float('inf')  #initialize ans with negative infinity to track the maximum sum
    
        curr=0  #initialize curr with 0 to calculate the current sum
        prev=0  #initialize prev with 0 to keep track of sum of previous subarray
    
        for i in range(n):  #iterate through the given array
            
            if i<k:  #if current index i is less than k
                
                curr+=a[i]  #add the value at current index i to curr
                prev+=a[i]  #add the value at current index i to prev
                
            else:
                ans=max(ans,curr,prev)  #compare and update the maximum sum so far
    
                prev+=a[i]-a[i-k]  #subtract the value at i-k index from prev and add the value at current index i
                curr+=a[i]  #add the value at current index i to curr
                
                curr=max(curr,prev)  #check and update the current sum
    
        ans=max(ans,prev,curr)  #compare and update the maximum sum at the end
    
        return ans  
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends