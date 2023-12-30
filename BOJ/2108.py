import sys
input=sys.stdin.readline
n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

lst.sort()

sum = 0
for i in lst:
    sum += i

print(round(sum / n + 0.00001))
print(lst[int(n/2)])

dic =dict()
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

mx=max(dic.values())
mx_dic = []

for key, value in dic.items():
    if value == mx:
        mx_dic.append(key)

if len(mx_dic) == 1:
    print(mx_dic[0])
else:
    print(sorted(mx_dic)[1])


print(max(lst) - min(lst))


