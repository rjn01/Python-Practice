#code]
t = int(input())
for i in range(t):
    n,m = input().split()
    l1 = set(map(int,input().split()))
    l2 = set(map(int,input().split()))
    l3 = l1.union(l2)
    print(len(l3))
    