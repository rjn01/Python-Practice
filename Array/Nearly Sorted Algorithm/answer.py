#code
T = int(input())
for i in range(T):
    a,b = input().strip().split()
    x = list(map(int,input().strip().split()))
    print(*sorted(x))