class Solution:

	def count(self,arr, n, x):
		# code here
		if x in arr:
		    return(arr.count(x))
		else: 
		    return(0)



#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends