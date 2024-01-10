lst = [0] * 102
lst[1] = 1
lst[2] = 1
lst[3] = 1
lst[4] = 2
lst[5] = 2
lst[6] = 3

t = int(input())
for i in range(t):
    n = int(input())
    if n <= 6:
        print(lst[n])
    else:
        for i in range(7,n+1):
            lst[i] = lst[i-1] + lst[i-5]
        print(lst[n])
