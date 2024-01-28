n = int(input())
for i in range(n):
    money = int(input())
    quarter = int(money / 25)
    dime = int((money % 25) / 10)
    nickel = int((money % 25) % 10 / 5)
    penny = (money % 25) % 10 % 5
    print(quarter, dime, nickel, penny)