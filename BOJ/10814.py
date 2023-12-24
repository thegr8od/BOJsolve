#나이순 정렬

import sys
input=sys.stdin.readline

N = int(input())

lst = []

for i in range(N):
    lst.append(list(input().split()))

lst.sort(key = lambda x : int(x[0]))

for i in range(N) :
    print(lst[i][0], lst[i][1])