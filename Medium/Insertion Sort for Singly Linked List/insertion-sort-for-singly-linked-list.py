#User function Template for python3

class Solution:
    # Function to perform insertion sort on a linked list.
    def insertionSort(self, head):
        # Return the head if it is empty or only contains one node.
        if not head or not head.next:
            return head
        # Create a dummy node with a very large value and set it as the head of the sorted list.
        dummy = Node(float('inf'))
        dummy.next = head
        # Initialize two pointers, pre1 and ptr1, to keep track of the previous node and the current node in the original list.
        pre1 = head
        ptr1 = head.next
        # Iterate through the remaining nodes in the original list.
        while ptr1:
            # Initialize two pointers, pre2 and ptr2, to keep track of the previous node and the current node in the sorted list.
            pre2 = dummy
            ptr2 = dummy.next
            # Find the correct position to insert the current node in the sorted list.
            while ptr2 and ptr2 != ptr1 and ptr2.data <= ptr1.data:
                pre2 = ptr2
                ptr2 = ptr2.next
            # If the current node is already in the correct position, move to the next node in the original list.
            if ptr2 == ptr1:
                pre1 = ptr1
                ptr1 = ptr1.next
            # Otherwise, insert the current node in the correct position in the sorted list.
            else:
                # Update the next pointer of the previous node in the sorted list to the current node.
                pre2.next = ptr1
                # Insert the current node between the previous node and the current node in the sorted list.
                tmp = ptr1.next
                ptr1.next = ptr2
                ptr2 = ptr1
                ptr1 = tmp
                # Update the next pointer of the previous node in the original list to the next node.
                pre1.next = ptr1
        # Return the head of the sorted list.
        return dummy.next


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
INF = float("inf")
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = Node(INF)
        nodes = list(map(int, input().strip().split()))
        ptr = a
        for x in nodes:
            ptr.next = Node(INF)
            ptr = ptr.next
            ptr.data = x
        a = a.next
        ob=Solution()
        head = ob.insertionSort(a)
        printList(head)
# } Driver Code Ends