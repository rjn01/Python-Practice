
def majorityWins(arr, n,  x,y):
    # code here
    a = arr.count(x)
    b = arr.count(y)
    if a>b:
        return(x)
    elif b>a:
        return(y)
    else:
        return(min(x,y))
        
    

if __name__ == '__main__':
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        x,y=map(int,input().strip().split())
        
        print(majorityWins(arr,n,x,y))
        T-=1


