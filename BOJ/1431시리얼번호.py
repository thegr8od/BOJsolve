import sys
input = sys.stdin.readline

def sum_num(s):
    res = 0
    for i in s:
        if i.isdigit():
            res += int(i)
    return res

n = int(input())
data = [input().rstrip() for i in range(n)]
data.sort(key = lambda x:(len(x),sum_num(x), x))

print(*data)