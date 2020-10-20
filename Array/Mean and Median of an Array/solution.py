
import math


##Complete the below codes
def median(A,N):
    
    ##Your code here
    #If median is fraction then convert the median to integer and return
    
    A.sort()
    if  N/2==0:
        a = N/2+1
        return(A[int(a-1)])
        
    else:
        a = (N+1)/2
        return(A[int(a-1)])
        
    
    
    
def mean(A,N):
    ##Your code here
    b = sum(A)/N
    return(math.floor(b))

    
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        
        print(mean(a,N),median(a,N))
        
        T-=1
    
    




if __name__=="__main__":
    main()

