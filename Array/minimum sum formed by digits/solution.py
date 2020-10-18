#code
T = int(input())
for i in range(T):
    n = int(input())
    elem = list(map(int,input().split()))
    elem.sort()
    a = "".join([str(elem[i]) for i in range(0,len(elem),2)])
    b = "".join([str(elem[i]) for i in range(1,len(elem),2)])
    print(int(a)+int(b))
    
