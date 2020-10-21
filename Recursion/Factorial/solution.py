
def factorial(n):
    #code here
    if n == 1 or n==0:
        return(1)
    elif(n<0):
        return(-1)
    else:
        return(n * factorial(n-1))
    

if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        
        print(factorial(n))

