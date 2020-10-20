
def isSorted(arr,n):
    #code here
    if arr==sorted(arr) or arr==sorted(arr,reverse=True):
        return(1)
        
    else:
        return(0)
    

if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(isSorted(arr,n))

