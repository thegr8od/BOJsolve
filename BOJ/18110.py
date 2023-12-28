import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
if n == 0:
    print(0)
else:
    cut_num = round(n * 0.15 + 0.000001) 

    lst = []

    sum = 0
    for i in range(n):
        lst.append(int(input()))

    lst.sort()
    q = deque(lst)

    for i in range(cut_num):
        q.pop()
        q.popleft()
        n -= 2



    for i in q:
        sum += i

    print(round(sum/n + 0.000001))
