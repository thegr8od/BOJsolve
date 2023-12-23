N = int(input())
str = input()
lst = []
sum = 0

for i in str:
    lst.append(ord(i) - ord('a') +1)

for i in range(len(lst)):
    sum += (lst[i] * (31 ** i))

print(sum % 1234567891)


