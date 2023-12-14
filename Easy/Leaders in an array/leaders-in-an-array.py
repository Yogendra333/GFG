class Solution:
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        ans=[]
        maxx=A[N-1]
    
        for i in range(N-1,-1,-1):#We start traversing the array from last element.
            #Comparing the current element with the maximum element stored. 
            #If current element is greater than max, we add the element.
            if A[i]>=maxx:
                #Updating the maximum element.
                maxx=A[i]
                #Appending the current element.
                ans.append(maxx)
                
        #Reversing the array.
        ans.reverse()
        #returning the answer.
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends