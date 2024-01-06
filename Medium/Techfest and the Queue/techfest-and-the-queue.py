
from typing import List

class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        
        # Calculating smallest prime factors (spf) for every number from 1 to b
        spf = [i for i in range(b+1)]
        for i in range(2, b+1):
            if spf[i] == i:
                for j in range(i*i, b+1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        # Counting all prime factors of each number from a to b
        ans = 0
        for i in range(a, b+1):
            cnt = 0
            while i > 1:
                cnt += 1
                i //= spf[i]
            
            ans += cnt

        return ans
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=int(input())
        b=int(input())
        
        obj = Solution()
        res = obj.sumOfPowers(a,b)
        
        print(res)
        

# } Driver Code Ends