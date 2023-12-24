#숫자의 합

N = int(input())
str = list(input())
sum = 0

for i in range(len(str)):
    sum += int(str[i])

print(sum)
