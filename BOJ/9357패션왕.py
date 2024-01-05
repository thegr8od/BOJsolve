import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    dic = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in dic:
            dic[wear[1]].append(wear[0])
        else:
            dic[wear[1]] = [wear[0]]
    cnt = 1
    for k in dic:
        cnt *= (len(dic[k])+1)
    print(cnt-1)
