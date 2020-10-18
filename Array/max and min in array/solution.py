#code
T = int(input())
for i in range(T):
    x = int(input())
    y = list(map(int,input().split()))
    z = [min(y),max(y)]
    print(*z)
