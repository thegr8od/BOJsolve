#펠린드롬수
import sys
input = sys.stdin.readline


while True:
    N = input().strip()
    if N == "0":
        break
    elif N == N[::-1]:
        print("yes")
    else:
        print("no")

