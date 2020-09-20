
#code

T = int(input())   #number of test cases
for i in range(T):
    N = int(input())  # number of elements
    #taking number in form of list    
    L = list(map(int, input().strip().split()))
    
    k= []
    L=L[::-1]  #reversing the list
    max = L[0] #first number in the revesed list is the leader
    k.append(max)
    
    #finding the leader
    for i in range(1,N):
        if L[i]>=max:
            max=L[i]
            k.append(max)
    
    print(*k[::-1])
            
        
