class Solution:
    # This function merges two 
    # sorted arrays and returns 
    # inversion count in the arrays. 
    def merge(self, arr, temp, left, mid, right): 
    
    	inv_count = 0
    
    	i = left # index for left subarray 
    	j = mid # index for right subarray 
    	k = left # ndex for resultant subarray 
    	while ((i <= mid - 1) and (j <= right)): 
    	
    		if (arr[i] <= arr[j]): 
    			temp[k] = arr[i] 
    			i += 1
    			k += 1
    		else: 
    		
    			temp[k] = arr[j] 
    			k += 1
    			j += 1
    
    			inv_count = inv_count + (mid - i) 
    
    	# Copy the remaining elements of left 
    	# subarray (if there are any) to temp 
    	while (i <= mid - 1): 
    		temp[k] = arr[i] 
    		i += 1
    		k += 1
    
    	# Copy the remaining elements of right 
    	# subarray (if there are any) to temp 
    	while (j <= right): 
    		temp[k] = arr[j] 
    		k += 1
    		j += 1
    
    	# Copy back the merged elements 
    	# to original array 
    	for i in range(left, right + 1): 
    		arr[i] = temp[i] 
    
    	return inv_count 
    
    # An auxiliary recursive function 
    # that sorts the input array and 
    # returns the number of inversions 
    # in the array. 
    def _mergeSort(self,arr, temp, left, right): 
    
    	inv_count = 0
    	if (right > left): 
    	
    		# Divide the array into two parts 
    		# and call _mergeSortAndCountInv() 
    		# for each of the parts 
    		mid = (right + left) // 2
    
    		# Inversion count will be sum of 
    		# inversions in left-part, right-part x 
    		# and number of inversions in merging 
    		inv_count = self._mergeSort(arr, temp, left, mid) 
    		inv_count += self._mergeSort(arr, temp, 
    								mid + 1, right) 
    
    		# Merge the two parts 
    		inv_count += self.merge(arr, temp, left,	 
    						mid + 1, right) 
    
    	return inv_count 
    
    # This function sorts the input 
    # array and returns the number 
    # of inversions in the array 
    def countPairs(self,arr, n): 
    	
    	# Modify the array so that problem 
    	# reduces to count inversion problem. 
    	for i in range(n): 
    		arr[i] = i * arr[i] 
    
    	# Count inversions using same 
    	# logic as below post 
    	# https://www.geeksforgeeks.org/counting-inversions/ 
    	temp = [0] * n 
    	return self._mergeSort(arr, temp, 0, n - 1) 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob= Solution()
        print(ob.countPairs(a, n))

        T -= 1


if __name__ == "__main__":
    main()
    
# } Driver Code Ends