n = int(input())
sum = 0
cnt = 0
i = 1
flag = 0
while sum<n:
    sum += i
    i += 1
    cnt += 1
    if sum == n :
        print(cnt)
        flag += 1
        break

if flag == 0:
    print(cnt-1)

