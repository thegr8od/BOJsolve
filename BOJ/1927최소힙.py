import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    cmd = int(input())
    if cmd == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, cmd)
    
