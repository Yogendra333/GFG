#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def LCA(self, root, x, y):
        # base case
        if root is None:
            return None
        
        # If both x and y are smaller than data at current node, we call 
        # the function recursively for finding LCA in the left subtree.
        if x < root.data and y < root.data:
            return self.LCA(root.left, x, y)
        
        # If both x and y are greater than data at current node, we call 
        # the function recursively for finding LCA in the right subtree.
        if x > root.data and y > root.data:
            return self.LCA(root.right, x, y)
        
        # returning the lowest common ancestor.
        return root
    
    def pathToNode(self, root, node, path):
        path.append(root.data)
        if root.data == node.data:
            return
        elif node.data > root.data:
            self.pathToNode(root.right, node, path)
        else:
            self.pathToNode(root.left, node, path)
    
    def kthCommonAncestor(self, root, k, x, y):
        lca = self.LCA(root, x, y)
        path = []
        self.pathToNode(root, lca, path)
        path.reverse()
        if len(path) < k:
            return -1
        return path[k - 1]



#{ 
 # Driver Code Starts

#Initial Template for Python 3


from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to Build Tree
def buildTree(str):
    # Corner Case
    if len(str) == 0 or str[0] == 'N':
        return None

    # Creating list of strings from input string after splitting by space
    ip = str.split()

    # Create the root of the tree
    root = Node(int(ip[0]))

    # Push the root to the queue
    queue = deque()
    queue.append(root)

    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        currNode = queue.popleft()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            queue.append(currNode.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            queue.append(currNode.right)

        i += 1

    return root

for _ in range(int(input())):
    s = input()
    root = buildTree(s)
    k, x, y = map(int, input().split())
    if root is None:
        continue
    
    if root.left is None and root.right is None:
        continue
    
    ob = Solution()
    print(ob.kthCommonAncestor(root, k, x, y))


# } Driver Code Ends