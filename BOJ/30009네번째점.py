left_lst = []
right_lst =[]
for i in range(3):
    a, b = map(int, input().split())
    left_lst.append(a)
    right_lst.append(b)

for i in range(3):
    if left_lst.count(left_lst[i]) == 1:
        x4 = left_lst[i]
    if right_lst.count(right_lst[i]) == 1:
        y4 = right_lst[i]
    

print(x4,y4)