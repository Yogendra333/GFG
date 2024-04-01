from typing import Optional
from collections import deque

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def __init__(self):
        # Counter to keep the count of inversions.
        self.my_counter = 0
        self.index = 0

    # Function to sort and merge two parts of an array.
    def merge(self, a, p, q, r):
        l = q - p + 1
        a1 = a[p:q + 1]
        l2 = r - q
        a2 = a[q + 1:r + 1]

        left = 0
        right = 0
        k = p

        while left < l and right < l2:
            if a1[left] <= a2[right]:
                a[k] = a1[left]
                left += 1
            else:
                a[k] = a2[right]
                right += 1
                # Adding the inversions which is the number of elements which
                # are smaller than a2[right] in the a1 array.
                self.my_counter += (l - left)
            k += 1

        while left < l:
            a[k] = a1[left]
            k += 1
            left += 1

        while right < l2:
            a[k] = a2[right]
            k += 1
            right += 1

    # Function to merge sort the array
    def mergeSort(self, a, p, r):
        if p < r:
            q = (p + r) // 2
            self.mergeSort(a, p, q)
            self.mergeSort(a, q + 1, r)
            self.merge(a, p, q, r)

    # Function to count inversions in the array.
    def inversionCount(self, arr):
        n = len(arr)
        self.mergeSort(arr, 0, n - 1)
        res = self.my_counter
        self.my_counter = 0
        return res

    # Function to traverse the tree in in-order and store the node values in an array
    def inOrderStorage(self, root, arr):
        if root is not None:
            self.inOrderStorage(root.left, arr)
            arr.append(root.data)
            self.inOrderStorage(root.right, arr)

    # Function to count the number of pairs violating BST property
    def pairsViolatingBST(self, n, root):
        arr = []
        self.inOrderStorage(root, arr)
        return self.inversionCount(arr)



#{ 
 # Driver Code Starts

class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

# Function to Build Tree
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip=list(map(str,s.split()))

    # Create the root of the tree
    root=Node(int(ip[0]))
    size=0
    q=deque()

    # Push the root to the queue
    q.append(root)
    size=size+1

    # Starting from the second element
    i=1
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1

        # Get the current node's value from the string
        currVal=ip[i]

        # If the left child is not null
        if(currVal!="N"):

            # Create the left child for the current node
            currNode.left=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]

        # If the right child is not null
        if(currVal!="N"):

            # Create the right child for the current node
            currNode.right=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def inputTree():
    treeString=input().strip()
    root = buildTree(treeString)
    return root
def inorder(root):
    if (root == None):
       return
    inorder(root.left);
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        root = inputTree();
        
        obj = Solution()
        res = obj.pairsViolatingBST(n, root)
        
        print(res)
        

# } Driver Code Ends