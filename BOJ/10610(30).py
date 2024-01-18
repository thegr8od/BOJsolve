n = input()
lst = [int(i) for i in n]

lst.sort(reverse=True)
sum = 0
flag = 0
for i in lst:
    sum += i
    if i == 0:
        flag += 1


if (flag != 0 and sum % 3 == 0):
    print(*lst, sep='')
else:
    print(-1)
