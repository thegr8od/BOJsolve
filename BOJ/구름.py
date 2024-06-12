# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
data = list(map(int, input().split()))

std = data.index(max(data))
max_v = max(data)


flag = 0

for i in range(std):
	if data[i] > data[i+1]:
		flag = 1

		
		
for j in range(std, len(data)-1):
	if data[i] < data[i+1]:
		flag = 1

	
print(flag)
if flag != 0:
	print(0)
else:
	sum(data)