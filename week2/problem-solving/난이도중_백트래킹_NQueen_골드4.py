# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

import sys

n = int(sys.stdin.readline())

arr = [0] * n

def is_possible(col):
    for i in range(col):
        if (arr[col] == arr[i]):
            return False
        elif (abs(arr[col] - arr[i]) == abs(col - i)):
            return False
    return True

ans = 0
def NQueen(col):
    global ans
    if col == n:
        ans += 1
        return
    
    for i in range(n):
        arr[col] = i
        if is_possible(col):
            NQueen(col + 1)

NQueen(0)
print(ans)