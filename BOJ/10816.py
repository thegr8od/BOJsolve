import sys
input = sys.stdin.readline


N = int(input())
sang = list(map(int,input().split()))
M = int(input())
compare = list(map(int,input().split()))

dict1 = {}

for i in sang:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

for i in compare:
    if i in dict1:
        print(dict1[i], end=' ')
    else:
        print(0, end=' ')


    