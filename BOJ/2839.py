N = int(input())

five_kg = 0
three_kg = 0

if (N % 5)%3 == 0:
    print(int((N//5) + (N % 5)/3))