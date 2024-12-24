
#User function Template for python3

class Solution:
    #Function to search a given number in a strictly sorted matrix.
    def searchMatrix(self, mat, x):
        n = len(mat)  # Number of rows
        m = len(mat[0])  # Number of columns

        left, right = 0, n * m - 1

        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = mat[mid // m][mid % m]  # Convert 1D index to 2D

            if mid_value == x:
                return 1  # Found the target
            elif mid_value < x:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        return 0  # Element not found



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends