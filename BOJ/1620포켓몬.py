import sys
input = sys.stdin.readline


dic = {}
n,m = map(int, input().split())

for i in range(1, n + 1):
    a = input().rstrip()
    dic[i] = a
    dic[a] = i
    
print(dic)
for j in range(m):
    cmd = input().rstrip()
    if cmd.isdigit():
        print(dic[int(cmd)])
    else:
        print(dic[cmd])