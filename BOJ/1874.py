import sys
input = sys.stdin.readline
n = int(input())
cur = 1
stack = []
answer = []
flag = 0

for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1

if flag == 0:
    for i in answer:
        print(i)

