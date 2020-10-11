
def immediateSmaller(arr,n,x):
    #return required ans
    if x in arr:
        arr.sort()
        a = arr.index(x)
        if a==0:
            return -1
        else:
            return(arr[a-1])
    else:
        arr.append(x)
        arr.sort()
        a = arr.index(x)
        if a==0:
            return -1
        else:
            return(arr[a-1])
    #code here


if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(e) for e in input().split()]
        x=int(input())
        
        ans=immediateSmaller(arr,n,x)
        print(ans)

