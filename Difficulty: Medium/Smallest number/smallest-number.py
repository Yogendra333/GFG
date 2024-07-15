#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:

    def smallestNumber(self, s, d):
        # code here
        # declare 10^D as initial number
        # start changing last digit and subtracting from the total sum
        if d * 9 < s:
            return "-1"

        n = 10**(d - 1)
        sum = s - 1
        temp = list(str(n))

        i = d - 1
        while i >= 0 and sum > 0:
            if sum > 9:
                temp[i] = '9'
                sum -= 9
            else:
                val = int(temp[i])
                val += sum
                temp[i] = str(val)
                sum = 0
            i -= 1

        return ''.join(temp)


#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends