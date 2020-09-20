#code

T = int(input())  #test case

for i in range(T):
    N,D = input().split() 

    #taking the elements in list
    l = list(map(int, input().strip().split()))

    #Splitting with respect to D
    x = l[int(D):]
    y = l[:int(D)]

    #Adding both list
    z = (x+y)
    
    print(*z)