# 큐 - 가운데를 말해요 (백준 골드2)
# 문제 링크: https://www.acmicpc.net/problem/1655

import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    left = list()
    right = list()
    ans = list()
    for i in range(n):
        x = int(sys.stdin.readline())

        if (len(left)<len(right)):
            if (x < right):
                heapq.heappush(left, -x)
                if left:
                    k = heapq.heappop(left)
                    heapq.heappush(right, -k)
            else:
                heapq.heappush(right, x)
        else:
            if (x < right):
                heapq.heappush(left, -x)
            else:
                heapq.heappush(right, x)
                if right:
                    k = heapq.heappop(right)
                    heapq.heappush(left, -k)


    print('\n'.join(ans))