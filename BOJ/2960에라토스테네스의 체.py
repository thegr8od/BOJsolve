n,k = map(int, input().split())
data = []

for i in range(1,n+1):
    data.append(i)
    
cnt = 0
for i in range(2,n+1):
    for j in data:
        if j % i == 0:
            data.remove(j)
            cnt += 1
            if cnt == k:
                print(j)
                
                
            
    