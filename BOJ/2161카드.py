from collections import deque

n = int(input())

card = [ i for i in range(1,n+1)]

card = deque(card)

while len(card) > 0:
    print(card.popleft(), end='')
    if len(card) != 0:
        card.append(card.popleft())


