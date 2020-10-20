
def maxSubArraySum(a,size):
    ##Your code here
    max_so_far = 0
    max_ending = 0
    '''for i in a:
        if i > 0:
            sum  = sum + i
        
    if sum == 0:
        return(max(a))
    else:
        return(sum)
    '''
    for i in a:
        max_ending = max_ending + i
        if max_so_far< max_ending:
            max_so_far = max_ending
        if max_ending<0:
            max_ending=0
    if max_so_far==0:
        return(max(a))
    else:
        return(max_so_far)
            



import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()

