class Solution:

	def kLargest(self,arr, n, k):
	    arr.sort(reverse=True)
	    arr = arr[:k]
	    return(arr)



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1
