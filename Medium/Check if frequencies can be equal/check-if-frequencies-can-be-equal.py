#User function Template for python3
class Solution:


	def getIdx(self,ch):
		return ord(ch) - ord('a')


	def allSame(self,freq, N):
		# get first non-zero element
		for i in range(0, N):
			if freq[i] > 0:
				same = freq[i]
				break

		# check equality of each element
		# with variable same
		for j in range(i + 1, N):
			if freq[j] > 0 and freq[j] != same:
				return False

		return True


	# Returns true if we can make all
	# character frequencies same
	def sameFreq(self,str1):
		l = len(str1)

		# fill frequency array
		freq = [0] * 26
		for i in range(0, l):
			freq[self.getIdx(str1[i])] += 1

		# if all frequencies are same,
		# then return true
		if self.allSame(freq, 26):
			return True

		# Try decreasing frequency of all character
		# by one and then check all equality of all
		# non-zero frequencies
		for i in range(0, 26):

			# Check character only if it
			# occurs in str
			if freq[i] > 0:
				freq[i] -= 1

				if self.allSame(freq, 26):
					return True
				freq[i] += 1

		return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends