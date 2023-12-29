import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))

lst = []

for i in range(N):
    weight, height = map(int, input().split())
    lst.append((weight, height))

for i in lst:
    grade = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            grade += 1
    print(grade, end = " ")

