class Solution:
    def __init__(self):
        self.st = ""
        self.name = 'A'

    # Function to print the parenthesis of matrix chain multiplication
    def printParenthesis(self, i, j, n, bracket):
        # If i and j are equal, it means only one matrix is remaining
        if i == j:
            self.st += self.name  # add the name of the matrix to the string
            self.name = chr(ord(self.name) + 1)  # increment the name for the next matrix
            return
        self.st += '('  # add '(' to the string
        self.printParenthesis(i, bracket[i][j], n, bracket)  # recursively print the parenthesis for the left side of the split
        self.printParenthesis(bracket[i][j] + 1, j, n, bracket)  # recursively print the parenthesis for the right side of the split
        self.st += ')'  # add ')' to the string

    # Function to calculate the minimum number of operations needed to multiply the matrices
    def matrixChainOrder(self, p, n):
        m = [[0] * n for _ in range(n)]  # create a 2D array to store the minimum number of operations
        bracket = [[0] * n for _ in range(n)]  # create a 2D array to store the split position for each matrix multiplication

        for i in range(1, n):
            m[i][i] = 0  # initialize the diagonal elements to 0

        for L in range(2, n):  # iterate over the lengths of the sequences
            for i in range(1, n - L + 1):  # iterate over the starting indices of the sequences
                j = i + L - 1  # calculate the ending index of the sequence
                m[i][j] = float('inf')  # set the minimum number of operations to a large value at first
                for k in range(i, j):  # iterate over possible split positions
                    q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]  # calculate the number of operations needed for this split
                    if q < m[i][j]:  # if this split has fewer operations than the current minimum, update the values
                        m[i][j] = q
                        bracket[i][j] = k

        self.printParenthesis(1, n - 1, n, bracket)  # call the function to print the parenthesis
        return self.st  # return the string containing the parenthesis


#{ 
 # Driver Code Starts

def get(p, n):
    m = [[0] * n for _ in range(n)]
    for i in range(1, n):
        m[i][i] = 0

    for L in range(2, n):
        for i in range(1, n - L + 1):
            m[i][i + L - 1] = float('inf')
            for k in range(i, i + L - 1):
                q = m[i][k] + m[k + 1][i + L - 1] + p[i - 1] * p[k] * p[i + L - 1]
                if q < m[i][i + L - 1]:
                    m[i][i + L - 1] = q

    return m[1][n - 1]

def find(s, p):
    arr = []
    ans = 0
    for t in s:
        if t == '(':
            arr.append((-1, -1))
        elif t == ')':
            b = arr.pop()
            a = arr.pop()
            arr.pop()
            arr.append((a[0], b[1]))
            ans += a[0] * a[1] * b[1]
        else:
            arr.append((p[ord(t) - ord('A')], p[ord(t) - ord('A') + 1]))

    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    ob = Solution()
    result = ob.matrixChainOrder(p, n)
    
    if find(result, p) == get(p, n):
        print("True")
    else:
        print("False")

# } Driver Code Ends