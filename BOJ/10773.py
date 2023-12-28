#제로
K = int(input())

# from collections import deque

lst = []



for i in range(K):
    num = int(input())
    if num != 0:
        lst.append(num)
    else:
        lst.pop()

sum = 0

for i in lst:
    sum += i

print(sum)

