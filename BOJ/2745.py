#검증수

lst = list(input().split())
sum = 0
for i in range(lst):
    sum += int(lst[i]) * int(lst[i])

print(sum%10)