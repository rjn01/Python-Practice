class Solution:
    def leftShops (self, i, L):
        # code here 
        return(2**L-i)
        

#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        i, L = input().split()
        i = int(i)
        L = int(L)
        ob = Solution()
        print(ob.leftShops(i, L))

