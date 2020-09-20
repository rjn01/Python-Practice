class Solution:

    def minValueToBalance(self,a,n):
        #code here.
        if len(a)%2==1:
            mid = int(len(a)+1/2)
        else:
            mid = int(len(a)/2)
        left = sum(a[:mid])
        right = sum(a[mid:])
        if left==right:
            return(0)
        else:
            return(abs(right-left))
        
t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)
