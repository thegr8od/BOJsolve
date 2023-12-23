N = int(input())

lst = []
for i in range(N):
    x , y = map(int, input().split())
    sub_list = []
    sub_list.append(x)
    sub_list.append(y)
    lst.append(sub_list)

lst.sort()

for i in range(len(lst)):
    print(*lst[i])


