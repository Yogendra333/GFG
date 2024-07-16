#User function Template for python3
class Solution:

    def printString(self, s, ch, count):
        i = 0
        while i < len(s) and count != 0:
            if s[i] == ch:
                count -= 1
            i += 1

        result = s[i:]

        return result if result != "" else ""

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends