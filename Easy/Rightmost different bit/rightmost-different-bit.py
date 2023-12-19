#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




    
# } Driver Code Ends
#User function Template for python3


class Solution:
    
    #Function to get rightmost set bit.
    def getRightMostSetBit(self,n):
        #returning the rightmost set bit of a number.  
        return math.log2(n&-n)+1
    
    #Function to find the first position with different bits.    
    def posOfRightMostDiffBit(self,m,n):
        
        #if numbers are same then -1 is returned.
        if m==n:
            return -1 
            
        #XOR operation only sets the dissimilar bits and unsets similar bits.
        #We do XOR operation on the numbers and return the rightmost set bit.   
        return self.getRightMostSetBit(m^n) 

#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        ob=Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends