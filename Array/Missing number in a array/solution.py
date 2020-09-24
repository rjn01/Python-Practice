
t = int(input())
for i in range(t):
    n = int(input())
    m = set(map(int,input().split()))
    l = set([i for i in range(1,n+1)])
    print(*(l-m))