

from typing import List

class Solution:

    def buyMaximumProducts(self, n: int, k: int, prices: List[int]) -> int:
        
        # Create a list of tuples, each containing the stock value and its limit
        stock_values_limits, res = [(prices[i], i + 1) for i in range(len(prices))], 0
        
        # Sort the stock_values_limits list based on stock value (ascending order)
        stock_values_limits.sort(key=lambda x: x[0])
        
        # Iterate over the sorted list
        for price, limit in stock_values_limits:
            # If k becomes zero or negative, or if the price is greater than k, break the loop
            if ((k <= 0) or (price > k)):
                break
            
            # Calculate the maximum number of stocks that can be bought within the limit or based on available funds
            temp = min(limit, (k // price))
            
            # Add the number of stocks bought to the result
            res += temp
            
            # Reduce the available funds by the cost of the bought stocks
            k -= (price * temp)
        
        # Return the total number of stocks bought
        return res



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
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends