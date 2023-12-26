from typing import List

class Solution:
    
    def sumZero(self, temp, starti, endj, n):
        presum = {}
        sum_val = 0
        max_length = 0
        for i in range(n):
            sum_val += temp[i]
            
            if temp[i] == 0 and max_length == 0:
                starti[0] = i
                endj[0] = i
                max_length = 1
            
            if sum_val == 0:
                if max_length < i + 1:
                    starti[0] = 0
                    endj[0] = i
                max_length = i + 1
            
            if sum_val in presum:
                old = max_length
                max_length = max(max_length, i - presum[sum_val])
                if old < max_length:
                    endj[0] = i
                    starti[0] = presum[sum_val] + 1
            else:
                presum[sum_val] = i
        
        return max_length != 0
    
    def sumZeroMatrix(self, a : List[List[int]]) -> List[List[int]]:
        row = len(a)
        col = len(a[0])
        temp = [0] * row
        
        fup, fdown, fleft, fright = 0, 0, 0, 0
        maxl = float('-inf')
        
        for left in range(col):
            temp = [0] * row
            for right in range(left, col):
                for i in range(row):
                    temp[i] += a[i][right]
                
                starti = [0]
                endj = [0]
                is_sum = self.sumZero(temp, starti, endj, row)
                ele = (endj[0] - starti[0] + 1) * (right - left + 1)
                
                if is_sum and ele > maxl:
                    fup = starti[0]
                    fdown = endj[0]
                    fleft = left
                    fright = right
                    maxl = ele
        
        ans = []

        if fup == fdown == fleft == fright == 0 and a[0][0] != 0:
            return ans
        
        for j in range(fup, fdown + 1):
            cnt = []
            for i in range(fleft, fright + 1):
                cnt.append(a[j][i])
            ans.append(cnt)

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



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        nm=IntArray().Input(2)
        
        
        a=IntMatrix().Input(nm[0], nm[1])
        
        obj = Solution()
        res = obj.sumZeroMatrix(a)
        if len(res) == 0:
            print(-1)
        else:
            IntMatrix().Print(res)
        

# } Driver Code Ends