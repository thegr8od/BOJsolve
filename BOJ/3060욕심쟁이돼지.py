t = int(input())
for i in range(t):
    day = 1  
    n = int(input())
    lst = list(map(int, input().split()))
    sum1 = sum(lst)
    while n >= sum1:
        day+=1
        sum1 = sum1 * 4
    print(day)
