def remove_duplicate(n, arr):
    #Code here
    x = list(set(arr))
    arr.clear()
    x.sort()
    arr = [arr.append(i) for i in x]
    n = len(arr)
    return n





if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        n = remove_duplicate(n, arr)
        for i in range(n):
            print (arr[i], end=" ")
        print()



