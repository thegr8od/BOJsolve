n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

oil = 0
minPrice=price[0]

for i in range(n-1):
    if minPrice>price[i]:
        minPrice=price[i]
    oil+=(minPrice*dis[i])

print(oil)