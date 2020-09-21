#code

T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().strip().split()))
    p = int(input())
    
    arr = sorted(arr)
    print(arr[p-1])