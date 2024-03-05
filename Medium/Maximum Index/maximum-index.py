#User function Template for python3

class Solution:
    #Function to find the maximum index difference.
    def maxIndexDiff(self,arr,n):
    
        #Constructing LMin[] such that LMin[i] stores the minimum value 
        #from (arr[0], arr[1], ... arr[i]).
        LMin=[0 for i in range(n)]
        LMin[0]=arr[0]
        for i in range(1,n):
            LMin[i] = min(arr[i],LMin[i-1])
    
        #Constructing RMax[] such that RMax[j] stores the maximum value 
        #from (arr[j], arr[j+1], ..arr[n-1]). 
        RMax=[0 for i in range(n)]
        RMax[n-1]=arr[n-1]
    
        for i in range(n-2,-1,-1):
            RMax[i]=max(arr[i],RMax[i+1])
    
        i,j,maxDiff=0,0,-1
        #Traversing both arrays from left to right to find optimum j-i. 
        #This process is similar to merge() of MergeSort.
        while j<n and i<n:
            if LMin[i]<=RMax[j]:
                #Updating the maximum difference.
                maxDiff=max(maxDiff,j-i)
                j=j+1
            else:
                i=i+1
        #returning the maximum difference.        
        return maxDiff


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends