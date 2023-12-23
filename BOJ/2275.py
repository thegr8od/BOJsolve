import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    floor = int(input()) #층
    hosu = int(input()) #호수
    people = [i for i in range(1, hosu+1)] #0층

    for j in range(floor):
        lst = []
        for k in range(hosu):
            lst.append(sum(people[:k+1])) # 아래층의 1~n호 까지의 합
        people = lst.copy()
    print(people[-1]) 







