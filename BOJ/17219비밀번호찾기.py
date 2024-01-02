import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dic = {}

for i in range(n):
    key, value = input().split()
    dic[key] = value

for j in range(m):
    key = input().rstrip()
    print(dic[key])